from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from lemon_service.api.ai_chat import ai_chat_router
from lemon_service.api.hotel import hotel_router
from lemon_service.api.user import user_router
from lemon_service.mcp_server import mcp_app
from lemon_service.middleware.auth import register_auth_middleware
from lemon_service.middleware.exception import register_exception_handlers

app = FastAPI(lifespan=mcp_app.lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源跨域（生产环境建议写具体域名）
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)
# 注册中间件
register_exception_handlers(app)
register_auth_middleware(app)
# 挂载api
app.include_router(hotel_router)
app.include_router(user_router)
app.include_router(ai_chat_router)
# 挂载mcp server
app.mount("/mcp-server", mcp_app)
