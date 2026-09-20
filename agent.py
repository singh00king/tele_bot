from llm import groq_llm
from tools import live_cricket_score

from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

memory = InMemorySaver()

agent = create_agent(
    model=groq_llm,
    tools=[live_cricket_score],
    checkpointer=memory,      # ← This is the important part
    system_prompt="You are a helpful assistant."
)