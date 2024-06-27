import streamlit as st
from pdf_loader import load_documents, split_documents
from database import add_to_db
from conversation_chain import get_conversation_chain
import io

def generate_response(user_input: str):
    if user_input and st.session_state.conversation:
        response = st.session_state.conversation({"question": user_input})
        return response['answer']
    else:
        return "Please upload and process a PDF file before asking a question."

def main():
    st.set_page_config(page_title='Local file Chatbot')
    st.title("Local file **Chatbot**")
    st.markdown("Ask any question about your **PDF file**!")

    if "uploaded_file" not in st.session_state:
        st.session_state.uploaded_file = None

    if "conversation" not in st.session_state:
        st.session_state.conversation = None    

    if "file_processed" not in st.session_state:
        st.session_state.file_processed = False

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            
    if prompt := st.chat_input():
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
            
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                placeholder = st.empty()
                with st.spinner("Thinking..."):
                    response = generate_response(prompt)
                    placeholder.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            
    with st.sidebar:
        st.header('Documents')
        uploaded_file = st.file_uploader("Upload your PDF file!", type=('pdf'))
        
        if uploaded_file and uploaded_file != st.session_state.uploaded_file:
            st.session_state.uploaded_file = uploaded_file
            st.session_state.file_processed = False
            
            bytes_data = uploaded_file.getvalue()
            file_stream = io.BytesIO(bytes_data)
            
            with st.spinner('Processing'):
                documents = load_documents(file_stream)
                if not documents:
                    st.error("No content could be loaded from the PDF.")
                else:
                    document_chunks = split_documents(documents)
                    if document_chunks:
                        try:
                            vectorstore = add_to_db(document_chunks)
                            conversation_retriever = vectorstore.as_retriever()
                            st.session_state.conversation = get_conversation_chain(conversation_retriever)
                            st.session_state.file_processed = True
                            st.success('File successfully uploaded and processed')

                        except Exception as X:
                            st.error('You need to have Ollama running! Launch Ollama and try again!')
                    else:
                        st.error("No readable content was found in the PDF.")

if __name__ == '__main__':
    main()
