import argparse
import logging
from utils import setup_logging
from process_files import process_folder

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate and update embeddings with metadata for files.")
    parser.add_argument("folder", type=str, help="Path to the folder containing files to process.")
    return parser.parse_args()

def main():
    setup_logging()
    args = parse_arguments()
    folder_path = args.folder
    process_folder(folder_path)

if __name__ == "__main__":
    main()

