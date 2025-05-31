import httpx
from fastapi.responses import StreamingResponse
from jinja2 import Template

from lemon_service.service.prompt import PromptService
from lemon_service.utils.date import get_current_datetime_str_cn


class AiChatService:
    __prompt_service = PromptService()

    async def send_message(self, message: str, conversation_id: str = ""):
        system_prompt_template = Template(self.__prompt_service.get_system_prompt())
        system_prompt = system_prompt_template.render(
            SYSTEM_CURRENT_TIME=get_current_datetime_str_cn()
        )

        chat_request_body = {
            "service_user_id": "lemon-hotel-demo",
            "system_prompt": system_prompt,
            "user_message": message,
            "used_tool_list": [
                {
                    "application_mcp_config_id": "72ea0b1fe8714f5cba628f036d4a95fb",
                    "tool_name": "__all__tools__"
                }
            ],
            "conversation_id": conversation_id,
        }

        target_url = "http://localhost:43210/chat/send-message"
        headers = {
            "Accept": "text/event-stream",
            "lemon-ai-api-key": "2dd76c971fc94f68add1a92965565b46",
            "Content-Type": "application/json"
        }

        async def event_stream():
            async with httpx.AsyncClient(timeout=None) as client:
                async with client.stream("POST", target_url, headers=headers, json=chat_request_body) as response:
                    async for line in response.aiter_lines():
                        if line.strip():
                            print("接收到数据：", line)
                            yield f"{line}\n\n"  # 注意 SSE 格式

        return StreamingResponse(event_stream(), media_type="text/event-stream")
