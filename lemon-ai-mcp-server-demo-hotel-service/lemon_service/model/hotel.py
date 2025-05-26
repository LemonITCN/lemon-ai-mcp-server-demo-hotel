from sqlalchemy import String
from sqlmodel import Field, Column

from lemon_service.base.base_model import BaseModel


class Hotel(BaseModel, table=True):
    """
    酒店
    """
    __tablename__ = 'lemon_hotel'
    name: str = Field(sa_column=Column(String(64), nullable=False, comment="酒店名称"))
    address: str = Field(sa_column=Column(String(256), nullable=False, comment="酒店地址"))
    description: str = Field(sa_column=Column(String(1024), nullable=False, comment="酒店介绍"))
