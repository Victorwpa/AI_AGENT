# from langchain.tools import Tool

from langchain_experimental.utilities import PythonREPL

python_repl=PythonREPL()

result = python_repl.run('print(10*2)')

print(result)
