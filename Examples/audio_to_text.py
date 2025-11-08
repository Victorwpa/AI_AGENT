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

audio = open('first_audio.mp3','rb')

transcription = client.audio.transcriptions.create(
    model='whisper-1',
    file = audio,
)

print(transcription.text)