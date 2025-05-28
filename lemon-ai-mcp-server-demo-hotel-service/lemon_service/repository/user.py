from sqlmodel import select

from lemon_service.base.base_repository import BaseRepository
from lemon_service.core.db_engine import create_db_session
from lemon_service.model import User


class UserRepository(BaseRepository[User]):
    """
    用户 数据访问
    """

    def __init__(self):
        super().__init__(User)

    def get_user_by_number(self, number: str):
        """
        通过账号获取用户
        :param number: 账号
        :return: 用户对象
        """
        with  create_db_session() as session:
            stmt = select(User).where(User.number == number)
            return session.exec(stmt).first()
