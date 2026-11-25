from dotenv import load_dotenv
import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
from langchain_tavily import TavilySearch
import tavily

load_dotenv()

tavily = TavilyClient()


@tool
def search(query: str) -> str:
    """
    Search the web for the query
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)



def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="Get the five jobs for java software engineering for 5 years of experience in chennai")]})
    print(result)
    


if __name__ == "__main__":
    main()
