from pathlib import Path
from google.cloud import storage

bucket_name = "sequence-analytics-reports-kp01"
report_path = Path(__file__).parent.parent / "reports" / "data_quality_report.html"
blob_name = f"reports/{report_path.name}"

client = storage.Client()
bucket = client.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_filename(str(report_path))

print("Uploaded to:", blob.name)
print("Bucket:", bucket_name)

