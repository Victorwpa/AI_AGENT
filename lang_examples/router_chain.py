import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -------------------------------- #

load_dotenv()

SECRET_KEY = os.getenv("API_KEY") #recuperando a chave da api de um dotenv

os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = ChatOpenAI(model='gpt-4o-mini')

classification_chain = (
    PromptTemplate.from_template(
        '''
        Classifique a pergunta do usuário em um dos seguintes setores:
        - Financeiro
        - Suporte Técnico
        - Outras Informações

        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

financial_chain = (
    PromptTemplate.from_template(
        '''
        Você é um especialista financeiro.
        Sempre responda começando com uma saudação do setor financeiro.
        Responda à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)


technical_chain = (
    PromptTemplate.from_template(
        '''
        Você é um especialista em TI.
        Sempre responda começando com uma saudação do setor de suporte técnico.
        Responda à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

other_info_chain = (
    PromptTemplate.from_template(
        '''
        Você é um assistente pessoal.
        Sempre responda começando com uma saudação ao usuário.
        Responda à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

def route(classification):
    classification = classification.lower()
    if 'financeiro' in classification:
        return financial_chain
    elif 'técnico' in classification:
        return technical_chain
    else:
        return other_info_chain
    
pergunta  = input('Olá! Qual sua dúvida?')

classification = classification_chain.invoke(
    {'pergunta':pergunta}
)

response_chain = route(classification=classification)

response = response_chain.invoke(
    {'pergunta':pergunta}
)

print(response)