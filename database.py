from embedding import get_embedding_function
from langchain.vectorstores import FAISS
import traceback


def add_to_db(chunks):
    try:
        #embeddings = HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-xl', model_kwargs={'device': 'mps'})
        vectorstore = FAISS.from_documents(chunks, get_embedding_function())
        return vectorstore
    except Exception as e:
        traceback.print_exc()
        return None

