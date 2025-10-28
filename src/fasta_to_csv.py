from Bio import SeqIO
import pandas as pd
from pathlib import Path

fasta_path = Path(__file__).parent.parent / "data" / "real_sequences.fasta"
csv_path = Path(__file__).parent.parent / "data" / "real_sequences.csv"

records = []
for record in SeqIO.parse(str(fasta_path), "fasta"):
    records.append({
        "sample_id": record.id,
        "gene": "TP53",
        "sequence": str(record.seq)
    })

df = pd.DataFrame(records)
df.to_csv(csv_path, index=False)
print("Saved:", csv_path)
print(df.head())

