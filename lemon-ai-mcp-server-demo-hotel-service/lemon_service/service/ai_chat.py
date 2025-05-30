import requests
from fastapi.responses import StreamingResponse


class AiChatService:
    """
    AI聊天 业务
    """

    def send_message(self, message: str, conversation_id: str = ""):
        """
        发送聊天消息
        :param conversation_id: 会话id
        :param message: 用户消息内容
        :return:
        """
        # 从原请求读取 JSON body
        chat_request_body = {
            "service_user_id": "lemon-hotel-demo",
            "system_prompt": "",
            "user_message": message,
            "used_tool_list": [
                {
                    "application_mcp_config_id", "72ea0b1fe8714f5cba628f036d4a95fb",
                    "tool_name", "list_all_hotel"
                }
            ],
            "conversation_id": conversation_id,
        }

        # 设置要请求的目标服务（Service B）
        target_url = "http://localhost:43210/chat/send-message"
        headers = {
            "Accept": "text/event-stream",
            "lemon-ai-api-key": "94803731e9204494b96aa9fd078dc448",
            "Content-Type": "application/json"
        }

        # 向目标服务发起 POST 请求，接收 Streaming 响应
        response = requests.post(target_url, headers=headers, json=chat_request_body, stream=True)

        # 转发 StreamingResponse
        return StreamingResponse(
            response.iter_content(chunk_size=1024),
            status_code=response.status_code,
            media_type=response.headers.get("Content-Type", "application/octet-stream")
        )
