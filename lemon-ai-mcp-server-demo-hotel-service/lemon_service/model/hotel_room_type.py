from sqlalchemy import String, Integer
from sqlmodel import Field, Column

from lemon_service.base.base_model import BaseModel


class HotelRoomType(BaseModel, table=True):
    """
    酒店房间类型
    """
    __tablename__ = 'lemon_hotel_room_type'
    name: str = Field(sa_column=Column(String(64), nullable=False, comment="酒店房间类型"))
    people_count: int = Field(sa_column=Column(Integer, nullable=False, comment="可入住人数"))
    description: str = Field(sa_column=Column(String(1024), nullable=False, comment="房间类型介绍"))
    price: int = Field(sa_column=Column(Integer, nullable=False, comment="房间价格,单位元"))
