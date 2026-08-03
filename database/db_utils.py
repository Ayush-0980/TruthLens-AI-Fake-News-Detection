import sqlite3

DB_PATH = "database/truthlens.db"

def save_prediction(
    headline,
    prediction,
    confidence
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO predictions
        (
            headline,
            prediction,
            confidence
        )
        VALUES (?, ?, ?)
        """,
        (
            headline,
            prediction,
            confidence
        )
    )

    conn.commit()
    conn.close()