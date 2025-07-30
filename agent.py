from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent,AgentExecutor
from tools import Tools
from dotenv import load_dotenv
from langchain import hub
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

load_dotenv()

#create a llm
llm=ChatOpenAI(temperature=0,model="gpt-3.5-turbo")

#prompt
prompt=hub.pull("hwchase17/react")

#create an agent
agent=create_react_agent(
    llm=llm,
    prompt=prompt
    ,tools=Tools
)
executor=AgentExecutor(
    agent=agent,
    tools=Tools,
    verbose=True
)
def run_agent(query):
    result = executor.invoke({"input": query})
    return result["output"]
