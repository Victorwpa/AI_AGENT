from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

#load .env variables

load_dotenv()

SECRET_KEY = os.getenv("API_KEY") #recuperando a chave da api de um dotenv

#Criando um client para poder usar um modelo e poder trabalhar com os LLMs
client = OpenAI(
    api_key=SECRET_KEY
)


img = client.images.generate(
    model="dall-e-3",
    prompt="Um biscoito tomando água",
    n=1,
    size="1024x1024",
    quality='standard'
)

# image_bytes = base64.b64decode(img.data[0].b64_json)
# with open("output.png", "wb") as f:
#     f.write(image_bytes)

image_url=img.data[0].url
print(image_url)
