from lemon_service.base import LemonBaseSchema


class LoginReqSchema(LemonBaseSchema):
    """
    登录请求
    """
    number: str
    password: str


class LoginRespSchema(LemonBaseSchema):
    """
    登录响应
    """
    token: str = ''
