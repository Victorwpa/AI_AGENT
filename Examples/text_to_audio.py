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
# ['alloy', 'ash', 'ballad', 'coral', 'echo', 'sage', 'shimmer', 'verse', 'marin', 'cedar'] # avaiable voice types
response = client.audio.speech.create(
    model='tts-1',
    voice='nova',
    input='Não pode desistir nunca. Elas dependem de você',
    instructions= 'be gentile, as one mother'
)

response.write_to_file('fist_audio.mp3')