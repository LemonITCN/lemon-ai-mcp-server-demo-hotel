from datetime import datetime

from sqlalchemy import String, Date
from sqlmodel import Field, Column

from lemon_service.base.base_model import BaseModel


class HotelRoomUseRecord(BaseModel, table=True):
    """
    酒店房间入住记录（含预约）
    """
    __tablename__ = 'lemon_hotel_room_use_record'
    hotel_id: str = Field(sa_column=Column(String(64), nullable=False, comment="酒店ID"))
    hotel_room_id: str = Field(sa_column=Column(String(64), nullable=False, comment="酒店房间ID"))
    client_name: str = Field(sa_column=Column(String(64), nullable=False, comment="客人姓名"))
    use_start_date: datetime = Field(sa_column=Column(Date, nullable=False, comment="入住开始日期"))
    use_end_date: datetime = Field(sa_column=Column(Date, nullable=False, comment="入住结束日期"))
    order_id: str = Field(sa_column=Column(String(64), nullable=False, comment="订单ID"))
