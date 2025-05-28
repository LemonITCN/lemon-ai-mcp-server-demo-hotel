from lemon_service.base.base_repository import BaseRepository

from lemon_service.model import UserSession


class UserSessionRepository(BaseRepository[UserSession]):
    """
    用户 数据访问
    """

    def __init__(self):
        super().__init__(UserSession)
