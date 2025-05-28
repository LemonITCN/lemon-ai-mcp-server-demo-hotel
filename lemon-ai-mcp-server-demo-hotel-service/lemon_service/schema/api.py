from typing import Optional

from lemon_service.base import LemonBaseSchema
from lemon_service.core import JSONLike


class ApiResponse(LemonBaseSchema):
    body: Optional[JSONLike] = None
    message: str = ''
    code: str = ''
    success: bool = True
