from datetime import datetime

from sqlalchemy import and_
from sqlmodel import select

from lemon_service.base.base_repository import BaseRepository
from lemon_service.core.db_engine import create_db_session
from lemon_service.model import HotelRoomUseRecord


class HotelRoomUseRecordRepository(BaseRepository[HotelRoomUseRecord]):
    """
    酒店房间入住、预约记录 数据访问
    """

    def __init__(self):
        super().__init__(HotelRoomUseRecord)

    def list_hotel_room_all_use_record(self, hotel_room_id: str):
        """
        列出酒店房间的所有入住、预约记录
        :param hotel_room_id: 酒店房间id
        :return: 房间列表
        """
        with create_db_session() as session:
            statement = (
                select(HotelRoomUseRecord)
                .where(HotelRoomUseRecord.hotel_room_id == hotel_room_id)
                .order_by(HotelRoomUseRecord.use_start_date)
            )
            return session.exec(statement).all()

    def list_hotel_time_range_all_use_record(self, hotel_id: str, query_start_date: datetime, query_end_date: datetime):
        """
        列出指定时间段内酒店房间的所有入住、预约记录
        :param hotel_id: 酒店id
        :param query_start_date: 查询时间段-开始时间
        :param query_end_date: 查询时间段-结束时间
        :return: 预约、入住记录
        """
        with create_db_session() as session:
            statement = (
                select(HotelRoomUseRecord)
                .where(HotelRoomUseRecord.hotel_id == hotel_id)
                .where(
                    and_(
                        HotelRoomUseRecord.use_start_date <= query_end_date,
                        HotelRoomUseRecord.use_end_date >= query_start_date
                    )
                )
                .order_by(HotelRoomUseRecord.use_start_date)
            )
            return session.exec(statement).all()
