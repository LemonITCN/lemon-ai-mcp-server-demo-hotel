from fastmcp import FastMCP

# 创建mcp服务器，然后挂载到fastapi中
mcp = FastMCP("lemon-ai-hotel-mcp-server")
mcp_app = mcp.http_app(path='/endpoint')
