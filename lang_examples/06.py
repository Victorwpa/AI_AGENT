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

prompot_template = PromptTemplate.from_template(
    'Me fale sobre o foguete {rocket}'
)

# runnable_sequence = prompot_template | model | StrOutputParser()

# rocket = input('Escolha o modelo de foguete a ser pesquisado: ')
# response = runnable_sequence.invoke(
#     {'rocket':rocket}
# )

# print(response)

chain = (
    PromptTemplate.from_template(
    'Me fale sobre o foguete {rocket}'
    )
    |model
    |StrOutputParser()
)

rocket = input('Escolha o modelo de foguete a ser pesquisado: ')
response = chain.invoke(
    {'rocket':rocket}
)

print(response)
