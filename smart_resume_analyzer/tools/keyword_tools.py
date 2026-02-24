import re
from google.adk.tools import FunctionTool

def extract_keywords(text: str) -> list:
    """
    Extract important keywords from text.
    """
    words = re.findall(r'\b[A-Za-z]{4,}\b', text.lower())
    return list(set(words))

keyword_tool = FunctionTool.from_function(extract_keywords)