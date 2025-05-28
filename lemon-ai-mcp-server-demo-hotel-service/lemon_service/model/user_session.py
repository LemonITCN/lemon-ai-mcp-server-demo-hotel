from datetime import datetime

from sqlalchemy import String, DateTime
from sqlmodel import Field, Column

from lemon_service.base.base_model import BaseModel


class UserSession(BaseModel, table=True):
    """
    用户会话
    """
    __tablename__ = 'lemon_user_session'
    user_id: str = Field(sa_column=Column(String(64), nullable=False, comment="用户ID"))
    token: str = Field(sa_column=Column(String(64), nullable=False, comment="会话令牌"))
    expire_time: datetime = Field(sa_column=Column(DateTime, nullable=False, comment="会话过期时间"))
