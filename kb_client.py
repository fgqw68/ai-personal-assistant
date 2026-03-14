import os
from docx import Document

KNOWLEDGE_BASE_PATH = "knowledge_base.docx"


async def list_mcp_tools():
    return []


def read_knowledge_base() -> str:
    """
    Read and return the content of knowledge_base.docx.

    Returns:
        str: The content of the knowledge base document as a string.

    Raises:
        FileNotFoundError: If the knowledge_base.docx file doesn't exist.
        Exception: If there's an error reading the document.
    """
    if not os.path.exists(KNOWLEDGE_BASE_PATH):
        raise FileNotFoundError(f"Knowledge base file not found: {KNOWLEDGE_BASE_PATH}")

    try:
        doc = Document(KNOWLEDGE_BASE_PATH)
        content = []

        # Read all paragraphs from the document
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():  # Only include non-empty paragraphs
                content.append(paragraph.text)

        return "\n\n".join(content)  # Join paragraphs with double newlines

    except Exception as e:
        raise Exception(f"Error reading knowledge base: {str(e)}")


async def read_knowledge_base_async() -> str:
    """
    Async wrapper for read_knowledge_base.
    Allows the function to be called in async contexts.
    """
    return read_knowledge_base()