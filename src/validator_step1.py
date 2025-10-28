import pandas as pd
from pathlib import Path

# set up the file path
data_path = Path(__file__).parent.parent / "data" / "sequences_sample.csv"

# load the CSV
df = pd.read_csv(data_path)

print("=== Data Preview ===")
print(df.head(), "\n")

# basic info
print("Total rows:", len(df))
print("Missing values per column:")
print(df.isna().sum(), "\n")

# duplicate detection
dupes = df.duplicated(subset=["sequence"])
print("Duplicate sequences found:", dupes.sum())
if dupes.any():
    print(df[dupes])

