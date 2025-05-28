from sqlalchemy import String
from sqlmodel import Field, Column

from lemon_service.base.base_model import BaseModel


class User(BaseModel, table=True):
    """
    用户
    """
    __tablename__ = 'lemon_user'
    number: str = Field(sa_column=Column(String(64), nullable=False, comment="账号", unique=True))
    password: str = Field(sa_column=Column(String(64), nullable=False, comment="密码密文"))
