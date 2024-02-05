import sqlite3
import json
from config import DATABASE_PATH

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def insert_text_slice_into_db(conn, text, page, paragraph, sentence, text_type, file_path, embedding):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS text_slices (
            id INTEGER PRIMARY KEY,
            text TEXT NOT NULL,
            page INTEGER,
            paragraph INTEGER,
            sentence INTEGER,
            type TEXT NOT NULL,
            file_path TEXT NOT NULL,
            embedding TEXT NOT NULL
        )
    """)
    cursor.execute("""
        INSERT INTO text_slices (text, page, paragraph, sentence, type, file_path, embedding)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (text, page, paragraph, sentence, text_type, file_path, json.dumps(embedding)))
    conn.commit()
