import pandas as pd
import re
from pathlib import Path

# path setup
data_path = Path(__file__).parent.parent / "data" / "sequences_sample.csv"
df = pd.read_csv(data_path)

# clean whitespace and standardize casing
df["sequence"] = df["sequence"].astype(str).str.strip().str.upper()

# define valid bases (A, T, G, C)
valid_pattern = re.compile(r"^[ATGC]+$")

def validate_sequence(seq):
    """Return True if sequence only contains A/T/G/C, else False."""
    if pd.isna(seq) or seq == "" or seq.lower() == "nan":
        return False
    return bool(valid_pattern.match(seq))

df["valid_sequence"] = df["sequence"].apply(validate_sequence)

print("=== DNA Sequence Validation ===")
print(df[["sample_id", "sequence", "valid_sequence"]], "\n")

invalid = df[~df["valid_sequence"]]
print("Invalid sequences found:", len(invalid))
if not invalid.empty:
    print(invalid[["sample_id", "sequence"]])

