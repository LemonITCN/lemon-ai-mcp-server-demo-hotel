from lemon_service.base import LemonBaseSchema


class AiChatSendMessageReq(LemonBaseSchema):
    """
    发送聊天消息请求
    """
    message: str
    conversationId: str
