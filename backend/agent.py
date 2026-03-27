from dotenv import load_dotenv
from langchain.tools import tool
from tavily import TavilyClient
from typing import Dict, Any
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver
from sentence_transformers import CrossEncoder
import torch

load_dotenv()

tavily = TavilyClient()

_cross_encoder = CrossEncoder("BAAI/bge-reranker-large")


@tool
def search_info_on_web(query:str)->Dict[str, Any]:
    """Search information on the web and return re-ranked results for better answer quality"""
    hits = tavily.search(query, max_results=8).get("results", [])

    scores = torch.sigmoid(
        torch.tensor(
            _cross_encoder.predict([[query, h.get("content", "")] for h in hits])
        )
    ).tolist()

    ranked = sorted(zip(scores, hits), key=lambda x: x[0], reverse=True)

    return {
        "query": query,
        "results": [
            {"title": h.get("title"), "url": h.get("url"), "content": h.get("content"), "score": round(score, 4)}
            for score, h in ranked[:3]
        ]
    }

def agent_creation():
    prompt = """You are an ai assistant with access to web search and up-to-date data retrieval. The user will give you a questions about a domain they care about(tech, news, sports, etc.). 
    Using the search info on web tool, search the web for the latest information relevant to their question. Return a clear, accurate answer to the user and offer more information or details if requested."""

    agent = create_agent(
        model=ChatOllama(model="qwen3",base_url="http://ollama:11434"),
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