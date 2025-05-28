from fastapi import APIRouter
from fastapi import Request

from lemon_service.schema.api import ApiResponse
from lemon_service.schema.auth import LoginReqSchema
from lemon_service.service.user import UserService

user_router = APIRouter(prefix="/user", tags=["用户API"])

user_service = UserService()


@user_router.post("/login", summary="用户登录")
async def login(data: LoginReqSchema, reqeust: Request = None):
    return ApiResponse(body=user_service.login(data))
