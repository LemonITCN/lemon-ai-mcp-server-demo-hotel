from typing import Union, Dict, List, Any

from pydantic import BaseModel

JSONLike = Union[
    BaseModel,
    Dict[str, Any],
    List[Any],
    str, int, float, bool, None
]


class ServiceException(Exception):
    """
    业务异常
    """

    def __init__(self, status_code: int, err_code: str, message: str):
        self.status_code = status_code
        self.err_code = err_code
        self.message = message
