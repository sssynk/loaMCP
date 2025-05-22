from fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

mcp = FastMCP("Library of Aletheia")

@mcp.tool()
def search_books(search_term: str):
    """Search for books with the given search_term. Returns a list of books and their data."""
    url = "https://searchv2.aletheia.foundation/collections/books/documents/search"
    headers = {
        "X-TYPESENSE-API-KEY": os.environ.get("SEARCH_KEY")
    }
    params = {
        "q": search_term,
        "query_by": "contents,title,author,tags",
        "page": 1,
        "page_size": 10
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()

@mcp.tool()
def get_book(book_id: str):
    """Get a book with the given book_id (in uuidv4 format)"""
    url = f"https://api.aletheia.foundation/books/{book_id}"
    headers = {
        "Authorization": f"Bearer {os.environ.get('ALETHEIA_KEY')}"
    }

    response = requests.get(url, headers=headers)
    return response.json()

@mcp.tool()
def get_user(user_name: str):
    """Search users by their Roblox username."""
    url = f"https://api.aletheia.foundation/users/search/{user_name}"
    headers = {
        "Authorization": f"Bearer {os.environ.get('ALETHEIA_KEY')}"
    }

    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=6622, path="/mcp")
