from fastapi.responses import JSONResponse

from lemon_service.core.api import ServiceException
from lemon_service.schema.api import ApiResponse


def register_exception_handlers(app):
    """
    注册异常处理器
    :param app: app对象
    """

    @app.exception_handler(ServiceException)
    async def service_exception_handler(request, exc: ServiceException):
        return JSONResponse(
            status_code=400,
            content=ApiResponse(
                code=exc.err_code,
                message=exc.message,
                success=False,
                body={}
            ).model_dump()
        )
