import sqlite3
from pathlib import Path

db_path = Path(__file__).parent.parent / "governance.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS run_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_timestamp TEXT,
  dataset_name TEXT,
  total_rows INTEGER,
  invalid_sequences INTEGER,
  duplicates INTEGER,
  missing_values INTEGER,
  score REAL,
  report_path TEXT
)
""")
conn.commit()
conn.close()
print(f"DB ready at: {db_path}")

