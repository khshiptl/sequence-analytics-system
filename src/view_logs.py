import sqlite3
from pathlib import Path
import pandas as pd

db_path = Path(__file__).parent.parent / "governance.db"
conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT id, run_timestamp, dataset_name, total_rows, invalid_sequences, duplicates, missing_values, score FROM run_log ORDER BY id DESC", conn)
conn.close()
print(df.to_string(index=False))

