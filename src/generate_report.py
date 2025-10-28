import pandas as pd
import re
import sqlite3
from pathlib import Path
from jinja2 import Template
from datetime import datetime
from google.cloud import storage

data_path = Path(__file__).parent.parent / "data" / "real_sequences.csv"
report_path = Path(__file__).parent.parent / "reports" / "data_quality_report.html"
db_path = Path(__file__).parent.parent / "governance.db"
bucket_name = "sequence-analytics-reports-kp01"

df = pd.read_csv(data_path)
df["sequence"] = df["sequence"].astype(str).str.strip().str.upper()

valid_pattern = re.compile(r"^[ATGC]+$")

def validate_sequence(seq):
    if pd.isna(seq) or seq == "" or seq.lower() == "nan":
        return False
    return bool(valid_pattern.match(seq))

df["valid_sequence"] = df["sequence"].apply(validate_sequence)
df["is_duplicate"] = df.duplicated(subset=["sequence"])
df["length"] = df["sequence"].apply(len)
df["gc_content"] = df["sequence"].apply(lambda s: round((s.count("G") + s.count("C")) / len(s) * 100, 2) if len(s) > 0 else 0)

length_mean = df["length"].mean()
df["length_anomaly"] = df["length"].apply(lambda x: abs(x - length_mean) > 0.25 * length_mean)

missing_counts = df.isna().sum()
total_rows = len(df)
invalid_sequences = (~df["valid_sequence"]).sum()
duplicates = df["is_duplicate"].sum()
missing_total = missing_counts.sum()
score = round(100 - ((invalid_sequences + duplicates + missing_total) / max(total_rows, 1)) * 100, 2)

template = """
<html>
<head><title>Data Quality Report</title></head>
<body style="font-family: Arial; margin: 40px;">
<h2>Bioinformatics Data Governance and Quality Report</h2>
<p><b>Total Records:</b> {{ total_rows }}</p>
<p><b>Invalid Sequences:</b> {{ invalid_sequences }}</p>
<p><b>Duplicate Sequences:</b> {{ duplicates }}</p>
<p><b>Missing Values:</b> {{ missing_total }}</p>
<p><b>Data Quality Score:</b> {{ score }}%</p>
<p><b>Average Length:</b> {{ avg_length }}</p>
<p><b>Average GC Content:</b> {{ avg_gc }}%</p>
<hr>
<h3>Invalid Sequences</h3>
{{ invalid_table }}
</body>
</html>
"""

invalid_table = df.loc[~df["valid_sequence"], ["sample_id", "sequence"]].to_html(index=False)
html = Template(template).render(
    total_rows=total_rows,
    invalid_sequences=invalid_sequences,
    duplicates=duplicates,
    missing_total=missing_total,
    score=score,
    invalid_table=invalid_table,
    avg_length=round(df["length"].mean(), 2),
    avg_gc=round(df["gc_content"].mean(), 2)
)

with open(report_path, "w") as f:
    f.write(html)

client = storage.Client()
bucket = client.bucket(bucket_name)
blob_name = f"reports/{report_path.name}"
blob = bucket.blob(blob_name)
blob.upload_from_filename(str(report_path))
gcs_uri = f"gs://{bucket_name}/{blob_name}"

conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute(
    """
    INSERT INTO run_log (run_timestamp, dataset_name, total_rows, invalid_sequences, duplicates, missing_values, score, report_path)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        datetime.utcnow().isoformat(timespec="seconds") + "Z",
        data_path.name,
        int(total_rows),
        int(invalid_sequences),
        int(duplicates),
        int(missing_total),
        float(score),
        gcs_uri,
    ),
)
conn.commit()
conn.close()

print("Report generated and uploaded")
print("GCS URI:", gcs_uri)

