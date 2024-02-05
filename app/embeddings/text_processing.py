import fitz  # Correct import for PyMuPDF
from nltk.tokenize import sent_tokenize

def process_pdf_pages(file_path):
    """
    Extracts text by pages, paragraphs, and sentences from a PDF file.
    Args:
        file_path (str): Path to the PDF file.
    Yields:
        dict: Information about each text slice, including text and metadata.
    """
    try:
        with fitz.open(file_path) as doc:
            for page_num, page in enumerate(doc, start=1):
                page_text = page.get_text("text")
                paragraphs = page_text.split('\n\n')
                for para_num, paragraph in enumerate(paragraphs, start=1):
                    sentences = sent_tokenize(paragraph)
                    for sent_num, sentence in enumerate(sentences, start=1):
                        yield {
                            'text': sentence,
                            'page': page_num,
                            'paragraph': para_num,
                            'sentence': sent_num,
                            'type': 'sentence'
                        }
    except Exception as e:
        print(f"Error processing PDF file {file_path}: {e}")

def process_plain_text(file_path):
    """
    Extracts text by paragraphs and sentences from a plain text file.
    Args:
        file_path (str): Path to the plain text file.
    Yields:
        dict: Information about each text slice, including text and metadata.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        paragraphs = content.split('\n\n')
        for para_num, paragraph in enumerate(paragraphs, start=1):
            sentences = sent_tokenize(paragraph)
            for sent_num, sentence in enumerate(sentences, start=1):
                yield {
                    'text': sentence,
                    'page': None,  # No page concept in plain text
                    'paragraph': para_num,
                    'sentence': sent_num,
                    'type': 'sentence'
                }


