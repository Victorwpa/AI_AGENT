import os
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

from langchain_community.cache import InMemoryCache, SQLiteCache

from langchain_classic.globals import set_llm_cache


#load .env variables

load_dotenv()

SECRET_KEY = os.getenv("API_KEY") #recuperando a chave da api de um dotenv

os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = OpenAI()

# set_llm_cache(InMemoryCache()) # para caso o cahce seja realizado na memoria
set_llm_cache(
    SQLiteCache(database_path='openai_cache.db')
)

prompt = 'Fale uma curiosidade sobre engenharia aeroespacial'

response1 = model.invoke(input = prompt,
                         temperature = 1.2,
                         max_tokens = 500)
print(f'Chamada 1: {response1}')

response2 = model.invoke(prompt)
print(f'Chamada 2: {response1}')