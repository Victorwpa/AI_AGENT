from config_loader import load_config
from openai import OpenAI
from dotenv import load_dotenv
import os

#load .env variables

load_dotenv()
config = load_config()

SECRET_KEY = os.getenv("API_KEY") #recuperando a chave da api de um dotenv

#Criando um client para poder usar um modelo e poder trabalhar com os LLMs
client = OpenAI(
    api_key=SECRET_KEY
)

stream_type = config["app"]["set_response_strem"]

# Para retornar um stream
stream = client.chat.completions.create(
    model = 'gpt-5-nano', #define qual modelo da OpenAI será usado
    messages = [
        {
            'role':'system',
            'content':'você é um engenheiro aeroespacial especialista em propulsao, fale tecnicamente'
        },
        {'role':'user',
         'content':'Sobre o motor raptor fale sobre sua construção, com foco em engenharia de materiais'
         }
    ], # seta que é um usuario passando a mensgem x
    stream=stream_type, # Parametro para liberar o streaming de responses, ao invés de esperar apenas um bloco 
    max_completion_tokens=5000 # configurando o máximo de tokens a serem usados nessa requisição

)


for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content,end='')