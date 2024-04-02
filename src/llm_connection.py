import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    
    """
    Call the LLM using API key. Here we are using Google Gemini Pro model
    
    Args: None
    
    Return: LLM model
    
    """
    
    load_dotenv()
    llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key = os.environ["GOOGLE_API_KEY"],temperature = 0.1)
    return llm