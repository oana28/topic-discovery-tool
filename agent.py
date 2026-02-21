from dotenv import load_dotenv
from langchain.tools import tool
from tavily import TavilyClient
from typing import Dict, Any
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

tavily = TavilyClient()

@tool
def search_info_on_web(query:str)->Dict[str, Any]:
    """Search information on the web"""
    return tavily.search(query)

def agent_creation():
    prompt = """You are an ai assistant with access to web search and up-to-date data retrieval. The user will give you a questions about a domain they care about(tech, news, sports, etc.). 
    Using the search info on web tool, search the web for the latest information relevant to their question. Return a clear, accurate answer to the user and offer more information or details if requested."""

    agent = create_agent(
        model=ChatOllama(model="qwen3"),
        tools=[search_info_on_web],
        system_prompt=prompt,
        checkpointer=InMemorySaver()
    )

    return agent

def get_config(thread_id:str):
    return {"configurable": {"thread_id":thread_id}}

def main():
    agent = agent_creation()
    config = get_config("1")
    while True:
        uinput = input("Write a question (or exit for quit): ")
        if uinput.lower() == "exit":
            break
        response = agent.invoke({"messages":[uinput]},config)
        print(response['messages'][-1].content)

main()