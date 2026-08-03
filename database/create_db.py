import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect(
    "database/truthlens.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    headline TEXT,
    prediction TEXT,
    confidence REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")