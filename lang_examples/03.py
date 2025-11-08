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

prompt = 'Fale uma curiosidade sobre engenharia aeroespacial'

response1 = model.invoke([
    SystemMessage(content = 'Você é um engenheiro aeroespacial sr com 40 anos de experiencia na indústria'),
    HumanMessage(content= prompt)
    ],
                            temperature = 1.2,
                            max_tokens = 500,
                            )
print(f'Chamada 1: {response1}')
