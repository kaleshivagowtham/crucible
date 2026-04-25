from langchain_community.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web for recent and relatable information on a topic. Returns Titles, Urls and Snippets."""
    results = tavily.search(query=query, max_results=5)

    return results

print(web_search.invoke("What are the recent news of war?"))