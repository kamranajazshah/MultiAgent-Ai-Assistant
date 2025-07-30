from langchain.agents import Tool
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain.tools import tool
import requests

#first tool
search=DuckDuckGoSearchAPIWrapper()
search_tool=Tool(
    name="DuckDuckGo Search",
    func=search.run,
    description="Search the web using DuckDuckGo"
)
#pythonTool
python=PythonREPLTool()

#weatherTool
@tool
def get_weather(city:str)->str:
 """ this tool is used to get weather updated from anywhere"""
 url = f"https://api.weatherstack.com/current?access_key=&query={city}"
 response=requests.get(url=url)
 return response.json()

Tools=[search_tool,python,get_weather]
