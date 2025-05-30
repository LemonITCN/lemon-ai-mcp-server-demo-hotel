from fastapi import APIRouter
from fastapi import Request

from lemon_service.schema.api import ApiResponse
from lemon_service.service.ai_chat import AiChatService

ai_chat_router = APIRouter(prefix="/ai-chat", tags=["客户AI聊天API"])

ai_chat_service = AiChatService()


@ai_chat_router.get("/send-message", summary="发送聊天消息")
async def login(message: str, conversation_id: str, reqeust: Request = None):
    return ApiResponse(body=ai_chat_service.send_message(message=message, conversation_id=conversation_id))
