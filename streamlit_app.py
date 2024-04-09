import streamlit as st
import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

#### Configuracion de la pagina web ####

st.title("ChatBOT de la Tesis Doctoral de Ignacio Sticco")
pregunta = st.text_input("Hacé tu pregunta", 'De que trata la tesis?')

st.write('Hola9')

#### Importacion y chunkeo de la base de datos ####

loader = TextLoader("./tesis_doctoral.txt", encoding='utf-8')
text_documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
documents = text_splitter.split_documents(text_documents)
embeddings = OpenAIEmbeddings()
vectorstore = DocArrayInMemorySearch.from_documents(documents, embeddings) # Embed the chunked documents

st.write(documents[0])
