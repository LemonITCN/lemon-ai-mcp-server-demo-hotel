from fastapi import Request

from lemon_service.core.api import ServiceException


def register_auth_middleware(app):
    """
    注册授权相关的中间件
    :param app: app对象
    """

    @app.middleware("http")
    async def auth_middleware(request: Request, call_next):
        route = request.scope.get("route")
        endpoint = getattr(route, "endpoint", None)

        if endpoint and getattr(endpoint, "_api_need_login", False):
            token = request.headers.get("LEMON-USER-TOKEN")
            if token != "valid-token":
                raise ServiceException(status_code=401, err_code="Unauthorized", message="Unauthorized")

        return await call_next(request)
