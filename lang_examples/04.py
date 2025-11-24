import os
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate


#load .env variables

load_dotenv()

SECRET_KEY = os.getenv("API_KEY") #recuperando a chave da api de um dotenv

os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = OpenAI()

template = '''
Traduza o texto do idioma {idioma1} para o {idioma2}:
{texto}
'''

prompt_template = PromptTemplate.from_template(
    template=template)

prompt = prompt_template.format(
    idioma1 = 'português brasil',
    idioma2 = 'russo',
    texto = 'Boa tarde!'
)

responde = model.invoke(prompt)

print(responde)

