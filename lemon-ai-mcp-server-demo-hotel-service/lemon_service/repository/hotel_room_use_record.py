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
