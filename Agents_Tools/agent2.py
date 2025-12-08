#Criando um agente com uma tool
#criando um python agent

import os
from langchain.tools import tool
from langchain_core.prompts import PromptTemplate
from langchain_experimental.utilities import PythonREPL
from langchain_experimental.agents.agent_toolkits import create_python_agent

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# -------------------------------- #

load_dotenv()

SECRET_KEY = os.getenv("API_KEY") #recuperando a chave da api de um dotenv

os.environ['OPENAI_API_KEY'] = SECRET_KEY

model = ChatOpenAI(model='gpt-4o-mini')

python_repl=PythonREPL()
python_repl_tool = tool(
    name_or_callable='Python REPL',
    description = 'one python shell. use this tool only to exec python codes. Execute only valid codes. If any return is need, use the print function',
    runnable= python_repl.run
)

agent_executor = create_python_agent(
    llm=model,
    tool=python_repl_tool,
    verbose=True,
    handle_parsing_errors=True,
)

prompt_template = PromptTemplate(
    input_variables=['query'],
    template='''
    Resolva o problema {query} e forneça o resultado. Use sempre a função print para mostrar o resultado final.
    '''
)

query = 'cateto oposto igual a cinco e adjacente igual a 10, quanto é a hipotenusa do triangulo retangulo?'

prompt = prompt_template.format(query=query)

response = agent_executor.invoke(prompt)

print(response)