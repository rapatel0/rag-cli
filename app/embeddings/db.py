import sqlite3
import json
from config import DATABASE_PATH

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def insert_text_slice_into_db(conn, text, page, paragraph, sentence, text_type, file_path, embedding):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO text_slices (text, page, paragraph, sentence, type, file_path, embedding)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (text, page, paragraph, sentence, text_type, file_path, json.dumps(embedding)))
    conn.commit()

