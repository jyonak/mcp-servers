"""
Resources are how you expose data to LLMs. 
They're similar to GET endpoints in a REST API - they provide data but 
shouldn't perform significant computation or have side effects:
"""

import requests
from fastmcp import FastMCP

# Create server
mcp = FastMCP("MCP Server with response options")


@mcp.resource("app://product/1")
def get_product() -> dict:
    """Fetch product data from dummyjson API and return as JSON"""
    response = requests.get('https://dummyjson.com/products/1')
    return response.json()


if __name__ == "__main__":
    # Start server
    mcp.run()
