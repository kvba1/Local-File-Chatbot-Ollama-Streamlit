from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from PyPDF2 import PdfReader

def load_documents(file_stream):
    pdf_reader = PdfReader(file_stream)
    documents = []
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            documents.append(Document(page_content=page_text))
        else:
            documents.append(Document(page_content=""))
    return documents

def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)