from openai import OpenAI
from dotenv import load_dotenv
import os

#load .env variables

load_dotenv()

SECRET_KEY = os.getenv("API_KEY") #recuperando a chave da api de um dotenv

#Criando um client para poder usar um modelo e poder trabalhar com os LLMs
client = OpenAI(
    api_key=SECRET_KEY
)

# Para retornar apenas uma mensagem
response = client.chat.completions.create(
    model = 'gpt-5-nano', #define qual modelo da OpenAI será usado
    messages = [
        # {'role':'user','content':'Sobre o motor raptor vaccum, explique porque ele é eficiente no vacuo'}
        {'role':'user','content':'Como eu configuro um arquivo .yaml dentro de uma estrutura python para salvar configurações e chamar ela depois'}
    ], # seta que é um usuario passando a mensagem x
    stream=False, # Parametro para liberar o streaming de responses, ao invés de esperar apenas um bloco 
    max_completion_tokens=5000 # configurando o máximo de tokens a serem usados nessa requisição
)
print(response.choices[0].message.content)