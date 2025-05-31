from fastapi import APIRouter
from fastapi import Request

from lemon_service.schema.ai_chat import AiChatSendMessageReq
from lemon_service.service.ai_chat import AiChatService

ai_chat_router = APIRouter(prefix="/ai-chat", tags=["客户AI聊天API"])

ai_chat_service = AiChatService()


@ai_chat_router.post("/send-message", summary="发送聊天消息")
async def login(data: AiChatSendMessageReq, reqeust: Request = None):
    return await ai_chat_service.send_message(message=data.message, conversation_id=data.conversationId)
