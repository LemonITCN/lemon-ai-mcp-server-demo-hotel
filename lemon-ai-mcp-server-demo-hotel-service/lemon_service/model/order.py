from sqlalchemy import String, Integer, Boolean
from sqlmodel import Field, Column

from lemon_service.base.base_model import BaseModel


class Order(BaseModel, table=True):
    """
    订单
    """
    __tablename__ = 'lemon_order'
    no: str = Field(sa_column=Column(String(64), nullable=False, comment="订单编号"))
    hotel_id: str = Field(sa_column=Column(String(64), nullable=False, comment="酒店ID"))
    total_price: int = Field(sa_column=Column(Integer, nullable=False, comment="订单总价格"))
    pay_state: bool = Field(sa_column=Column(Boolean, nullable=False, comment="支付状态，是否已经支付"))
