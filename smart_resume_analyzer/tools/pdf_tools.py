from pypdf import PdfReader
from google.adk.tools import FunctionTool

def extract_pdf_text(filepath: str) -> str:
    """
    Extract text from a PDF resume.
    """
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

pdf_tool = FunctionTool.from_function(extract_pdf_text)