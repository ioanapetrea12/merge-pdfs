# PDF Merge Tool

A Python script that automatically merges multiple PDF files into a single, ordered PDF.  
It applies custom rules to ensure the correct order:
- **Fisa** files come first
- **Tichet** files follow
- Other documents are appended alphabetically

This project demonstrates:
- File handling in Python
- Regex-based filename parsing
- Error handling for missing or corrupted PDFs
- Automation of repetitive document processing tasks

# Project Structure
- merge_pdfs.py       (main script, runs the PDF merge process)
- requirements.txt    (dependencies)
- pdfs/               (folder with input PDF files)
