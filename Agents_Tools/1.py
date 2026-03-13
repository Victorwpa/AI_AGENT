import os
from langchain.agents import create_agent
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# -------------------------------- #

load_dotenv()
SECRET_KEY = os.getenv("API_KEY")
os.environ['OPENAI_API_KEY'] = SECRET_KEY

# Modelo
model = ChatOpenAI(model='gpt-4')

# Conexão com o banco SQLite
db = SQLDatabase.from_uri('sqlite:///Agents_Tools/ipca.db')

# Toolkit SQL
toolkit = SQLDatabaseToolkit(
    db=db,
    llm=model,
)

# Prompt de sistema que obriga uso do banco
system_message = """
Você é um agente especializado em responder perguntas sobre o IPCA.
Sempre que receber uma pergunta, escreva e execute uma consulta SQL no banco ipca.db usando sua ferramenta SQL.
Nunca invente valores: todas as respostas devem vir do banco.
Explique brevemente o raciocínio e mostre o resultado final em português BR.
Se não encontrar dados, informe claramente que não há registros disponíveis.
"""

# Criação do agente
agent = create_agent(
    model=model,
    tools=toolkit.get_tools(),
    system_prompt=system_message
)

# Pergunta
question = "Qual mês e ano teve o maior IPCA?"

# Execução
output = agent.invoke("Qual mês e ano teve o maior IPCA?")

print(output.get("output", output))