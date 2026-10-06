from langchain.tools import tool
import requests
from dotenv import load_dotenv
import os
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
response = tavily_client.search("Who is Leo Messi?")
def web_search(query:str)->str:
    """search the web for recent and reliable information on topic ."""
    result=tavily_client.search(query=query,max_results=5)
    print(result)