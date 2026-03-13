import os
from langsmith import Client
from langchain.agents import create_agent
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# -------------------------------- #

load_dotenv()

SECRET_KEY = os.getenv("API_KEY") #recuperando a chave da api de um dotenv

os.environ['OPENAI_API_KEY'] = SECRET_KEY
## 
model = ChatOpenAI(model='gpt-4')
client=Client()

db = SQLDatabase.from_uri('sqlite:///Agents_Tools/ipca.db')
###

toolkit = SQLDatabaseToolkit(
    db=db,
    llm=model,
)

system_message = client.pull_prompt('hwchase17/react-chat',include_model=True).template

# system_message = """
# Você é um agente especializado em responder perguntas sobre o IPCA.
# Sempre que receber uma pergunta, utilize obrigatoriamente o banco de dados SQL conectado (ipca.db) através da sua tool.
# Nunca invente valores: todas as respostas devem vir de consultas SQL ao banco.
# Explique brevemente o raciocínio e mostre o resultado final em português BR.
# Se não encontrar dados, informe claramente que não há registros disponíveis.
# """

agent = create_agent(
    model = model,
    tools = toolkit.get_tools(),
    system_prompt=system_message
    )
prompt = ''' Responda ao questionamento: {q} .Relacionado ao IPCA em português BR.
'''
template = PromptTemplate.from_template(prompt)
question = 'qual mes e ano teve o maior IPCA? Use a ferramenta de sql'


output = agent.invoke(
    {'input': question}
)

# print(output.get('output'))
print(output)

# from sqlalchemy import create_engine, text

# engine = create_engine('sqlite:///Agents_Tools/ipca.db')
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM ipca "))
#     for row in result:
#         print(row)

