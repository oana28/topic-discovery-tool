from fastapi import FastAPI
from backend.agent import agent_creation, get_config
from pydantic import BaseModel
import asyncio 

app = FastAPI()
agent = agent_creation()

class AgentRequest(BaseModel):
    question: str

@app.post("/chat")
async def ask_question(agentRequest: AgentRequest):
    config = get_config("1")
    uinput = {"messages":[{"role": "user", "content": agentRequest.question}]}
    response = await asyncio.to_thread(agent.invoke, uinput, config)
    return response['messages'][-1].content