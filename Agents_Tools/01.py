from langchain_community.tools import DuckDuckGoSearchRun


ddg_search = DuckDuckGoSearchRun()

search_result = ddg_search.run('Qual os principais recursos da AWS')
print(search_result)


