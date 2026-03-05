from fastmcp import FastMCP

mcp = FastMCP("basic-mcp-server")

@mcp.tool()
def say_hello(name: str) -> str:
    """Greets the user by name"""
    return f"Hello, {name}! Welcome to your first MCP server."

if __name__ == "__main__":
    mcp.run()