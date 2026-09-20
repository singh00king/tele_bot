import os
from dotenv import load_dotenv
load_dotenv()
groq_key = os.getenv("API_KEY_3")
#
from langchain.chat_models import init_chat_model

#Groq
groq_llm = init_chat_model(
    model="openai/gpt-oss-20b",
    model_provider="groq",
    api_key=groq_key
)
groq_llm.invoke("What is a cat?")