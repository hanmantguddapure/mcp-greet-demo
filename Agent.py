import asyncio
from fastmcp import Client
from fastmcp.client.transports.stdio import StdioTransport
from openai import AsyncOpenAI

async def main():
    transport = StdioTransport(
        command="python",
        args=["d:/projects/AI/mcp/BasicExample.py"]
    )

    async with Client(transport=transport) as client:
        tools = await client.list_tools()
        print("Available tools:", tools)

        # Example: user asks a natural language question
        user_input = "Please greet Hanmant"

        # Call the MCP tool directly (instead of .to_openai)
        result = await client.call_tool("say_hello", {"name": "Hanmant"})
        print("Tool result:", result.data)

if __name__ == "__main__":
    asyncio.run(main())