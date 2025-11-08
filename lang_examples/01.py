import os
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

#load .env variables

load_dotenv()

SECRET_KEY = os.getenv("API_KEY") #recuperando a chave da api de um dotenv

os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = OpenAI()

response= model.invoke(
    input='me conte uma piada sobre engenharia aeroespacial',
    temperature = 1,
    max_tokens = 600,
)

print(response)