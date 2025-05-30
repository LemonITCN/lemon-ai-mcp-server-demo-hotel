from sqlalchemy import String
from sqlmodel import Field, Column

from lemon_service.base.base_model import BaseModel


class HotelRoom(BaseModel, table=True):
    """
    酒店房间
    """
    __tablename__ = 'lemon_hotel_room'
    no: str = Field(sa_column=Column(String(64), nullable=False, comment="房间编号"))
    hotel_id: str = Field(sa_column=Column(String(64), nullable=False, comment="酒店ID"))
    hotel_room_type_id: str = Field(sa_column=Column(String(64), nullable=False, comment="酒店房间类型ID"))
