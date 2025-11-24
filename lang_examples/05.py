import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

# -------------------------------- #

load_dotenv()

SECRET_KEY = os.getenv("API_KEY") #recuperando a chave da api de um dotenv

os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = ChatOpenAI(model='gpt-4o-mini')

# ----------------------------------- #

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system','Você deve responder baseado em dados geogŕaficos de regiões do Brasil.'),
        ('human','Por favor, me fale sobre a região {regiao}.'),
        ('ai','Claro, vou iniciar'),
        ('human','Certifique-se de inserir informações demográficos'),
        ('ai','Entendido. Aqui estão os dados')
    ]
)

# prompt = chat_template.format_messages(regiao='Centro Oeste')

response = model.invoke(chat_template.format(regiao='Centro Oeste'))

print(response.content)


