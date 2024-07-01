
# Local File Chatbot

The Local File Chatbot is a Streamlit-based application that allows users to interact with their local PDF files through a chatbot interface. The chatbot can answer questions about the contents of the uploaded PDF files, making it a useful tool for extracting and querying information from documents.

## Overview
Check out my YouTube video below:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/ySqWSsWC9iM/0.jpg)](https://www.youtube.com/watch?v=ySqWSsWC9iM)

## Installation

To run this project install all the requirements:

```bash
  pip install -r requirements.txt
```
Make sure you have installed Ollama model of your choice (e.g. Llama3) with:

```bash
ollama pull llama3
```

Change the model name variable for your according model in conversation_chain.py file:

```bash
model_name = 'llama3'
```



## Run Locally

Run the project with:

```bash
  streamlit run app.py
```
## License

[MIT](https://choosealicense.com/licenses/mit/)
