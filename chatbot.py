import streamlit as st
from PyPDF2  import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_text_splitters import RecursiveCharacterTextSplitter

#upload the file

st.header("My First Chatbot")
with st.sidebar:
    st.title("Your Document")
    file = st.file_uploader("upload the pdf file and start asking question", type ="pdf")

# Extract the Text

if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        #st.write(text)

#Break in to chunks

    text_splitter = RecursiveCharacterTextSplitter(
        separators = "\n",
        chunk_size = 1000,
        chunk_overlap=150,
        length_function=len
    )

    chunks = text_splitter.split_text(text)
    st.write(chunks)
