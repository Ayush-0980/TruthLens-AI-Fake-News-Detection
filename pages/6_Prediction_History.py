import streamlit as st
import sqlite3
import pandas as pd

st.title("📜 Prediction History")

conn = sqlite3.connect(
    "database/truthlens.db"
)

df = pd.read_sql_query(
    """
    SELECT *
    FROM predictions
    ORDER BY id DESC
    """,
    conn
)

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Predictions",
    len(df)
)

if len(df) > 0:

    fake_count = len(
        df[df["prediction"] == "Fake News"]
    )

    real_count = len(
        df[df["prediction"] == "Real News"]
    )

    col2.metric(
        "Fake News",
        fake_count
    )

    col3.metric(
        "Real News",
        real_count
    )

st.divider()

# Table
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# Download CSV
csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download History",
    data=csv,
    file_name="prediction_history.csv",
    mime="text/csv"
)

conn.close()