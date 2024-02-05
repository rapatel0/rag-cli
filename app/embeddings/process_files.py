import os
from db import get_db_connection, insert_text_slice_into_db
from embeddings import generate_embedding_for_text
from text_processing import process_pdf_pages, process_plain_text
from utils import setup_logging
import logging

def process_file(file_path, conn):
    if file_path.endswith('.pdf'):
        text_slices = process_pdf_pages(file_path)
    elif file_path.endswith('.txt') or file_path.endswith('.md'):
        text_slices = process_plain_text(file_path)
    else:
        logging.warning(f"Unsupported file type: {file_path}")
        return

    for text_slice in text_slices:
        embedding = generate_embedding_for_text(text_slice['text'])
        insert_text_slice_into_db(conn, text_slice['text'], text_slice['page'], text_slice['paragraph'],
                                  text_slice['sentence'], text_slice['type'], file_path, embedding)

def process_folder(folder_path):
    conn = get_db_connection()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                process_file(file_path, conn)
                logging.info(f"Processed file: {file_path}")
            except Exception as e:
                logging.error(f"Error processing file {file_path}: {e}")
    conn.close()

