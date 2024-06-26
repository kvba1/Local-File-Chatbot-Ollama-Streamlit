from langchain_community.embeddings.ollama import OllamaEmbeddings
#from langchain.embeddings import HuggingFaceInstructEmbeddings

def get_embedding_function():
    embeddings = OllamaEmbeddings(model='nomic-embed-text')
    #embeddings = HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-xl', model_kwargs = {'device': 'mps'})
    return embeddings
