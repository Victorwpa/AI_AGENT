import os
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

from langchain_community.cache import InMemoryCache, SQLiteCache

from langchain_classic.globals import set_llm_cache
from langchain_classic.schema import SystemMessage,HumanMessage

#load .env variables

load_dotenv()

SECRET_KEY = os.getenv("API_KEY") #recuperando a chave da api de um dotenv

os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = OpenAI()

# set_llm_cache(InMemoryCache()) # para caso o cahce seja realizado na memoria
set_llm_cache(
    SQLiteCache(database_path='openai_cache.db')
)

prompt = '''Estou estudando LLMs e cheguei na parte de RAG e embedding. Irei dar ao modelo de embedding um .pdf
 para que seja processado e vetorizado para que o modelo utilize futuramente para fornecer resultados.
 Sugira tres temas de fácil acesso (ex: guias, manuais, artigos) para que eu crie o meu primeiro vector database.
   Eu gosto de 
 Industria aeroespacial, tecnologia e curiosidades.
'''

response1 = model.invoke([
    SystemMessage(content = 'Você é um professor de engenharia de dados. Responda com temas especificos de nível introdutorio, para engajar o aluno'),
    HumanMessage(content= prompt)
    ],
                            temperature = 1.2,
                            max_tokens = 500,
                            )
print(f'Chamada 1: {response1}')
