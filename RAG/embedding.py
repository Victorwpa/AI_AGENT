from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
from langchain_chroma import Chroma
# from langchain import hub
from langsmith import Client
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
# -------------------------------- #

load_dotenv()

SECRET_KEY = os.getenv("API_KEY") #recuperando a chave da api de um dotenv

os.environ['OPENAI_API_KEY'] = SECRET_KEY
BASE_DIR = Path(__file__).resolve().parent
model = ChatOpenAI(
    model= 'gpt-4'
)
PDF = BASE_DIR / "DesenvolvimentoAvaliacaoChatbot.pdf"

loader = PyPDFLoader(PDF)
docs = loader.load()

text_splitter= RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap =200,
)
#Aqui o PDF é quebrado em pequenos pedaços (chunks)
chunks = text_splitter.split_documents(
    documents=docs,
)
# O que é embedding? é um modelo de representação numerica de texto que pode ser usado para medir o relacionamento
# entre dois pedaços de texto

#Agora, precisamos usar um modelo de embedding para realizar indexar e vetorizar num banco de vetores os chunks

embedding = OpenAIEmbeddings() 
vector_store = Chroma.from_documents(
    documents = chunks,
    embedding=embedding,
    collection_name = 'RAG_Article'
)
#Criar um retriever

retriever = vector_store.as_retriever()

# result = retriever.invoke(
#     'O que é RAG?'
# )

# print(result)
prompt = Client().pull_prompt('rlm/rag-prompt')

rag_chain = (
    {
        'context': retriever,
        'question':RunnablePassthrough()
    }
    | prompt
    | model
    | StrOutputParser()
)

# question = 'O que é RAG?'

# response = rag_chain.invoke(question)

try:
    while True:
        question = input('Qual a sua duvida? ')
        response = rag_chain.invoke(question)
        print(response)
except KeyboardInterrupt:
    exit()