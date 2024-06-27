from langchain_community.llms.ollama import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain

model_name = 'llama3'

def get_conversation_chain(_retriever):
    model = Ollama(model=model_name)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=model,
        memory=memory,
        retriever=_retriever,
    )
    return conversation_chain


