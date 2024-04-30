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

st.title("🚀 ChatBOT de la Tesis Doctoral de Ignacio Sticco 🚀")
st.write("#### Pregunta:")
pregunta = st.text_input("Hacé tu pregunta")
st.write("#### Respuesta:")


#### Importacion y chunkeo de la base de datos ####

loader = TextLoader("./tesis_doctoral.txt", encoding='utf-8')
text_documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
documents = text_splitter.split_documents(text_documents)
embeddings = OpenAIEmbeddings()
vectorstore = DocArrayInMemorySearch.from_documents(documents, embeddings) # Embed the chunked documents


#### Configuracion de la cadena ####
model = ChatOpenAI(openai_api_key=st.secrets["OPENAI_API_KEY"], model="gpt-3.5-turbo")
parser = StrOutputParser()

template = """
Respondé las preguntas basandote en el siguiente contexto. Si no podes responder una pregunta. 
Responde: "Necesito más información para responder esta pregunta.". 

Si te preguntan quienes son los directores respondé: Claudio Dorso y Guillermo Frank.

Si te preguntan cuáles son las conclusiones respondé algo semejante a este texto: 
"La conclusión es que los vestíbulos mejoran las evacuaciones de emergencia por dos motivos. 
Por un lado, incrementan el flujo de evacuación, por otro lado, disminuyen la presión que soportan los 
individuos. El aumento del flujo se debe al hecho que los vestíbulos son capaces de regular la densidad en 
la vecindad de la puerta de salida. La presi´on disminuye porque los vestíbulos obligan a la multitud a 
dispersarse más."


Contexto: {context}

Pregunta: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
setup = RunnableParallel(context=vectorstore.as_retriever(), question=RunnablePassthrough())
chain = (
    setup   
    | prompt
    | model
    | parser
)


#### Correr el programa en el front ####

if pregunta:
    response = chain.invoke(pregunta)
    st.write(response)

st.markdown("""---""")
st.write("#### Preguntas de ejemplo:")
st.write("- ¿De qué trata la tesis?")
st.write("- ¿Qué es la dinámica peatonal?")
st.write("- ¿Qué parámetros se ajustaron y cuáles son los valores óptimos?")
st.write("- ¿Cuál es la fórmula matemática de los blocking clusters?")
st.write("- ¿Cómo se pueden mejorar las evacuaciones de emergencia ?")

st.markdown("""---""")
st.write("Enlace a la tesis: https://bibliotecadigital.exactas.uba.ar/download/tesis/tesis_n7313_Sticco.pdf")

