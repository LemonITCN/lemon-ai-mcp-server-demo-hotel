from fastmcp import FastMCP

from .hotel_tools import register_all_hotel_tools

# 创建mcp服务器，然后挂载到fastapi中
mcp = FastMCP("lemon-ai-hotel-mcp-server")
mcp_app = mcp.http_app(path='/endpoint')

register_all_hotel_tools(mcp=mcp)
