from sqlmodel import select

from lemon_service.base.base_repository import BaseRepository
from lemon_service.core.db_engine import create_db_session
from lemon_service.model import HotelRoom


class HotelRoomRepository(BaseRepository[HotelRoom]):
    """
    酒店房间 数据访问
    """

    def __init__(self):
        super().__init__(HotelRoom)

    def list_hotel_all_room(self, hotel_id: str):
        """
        列出酒店的所有房间列表
        :param hotel_id: 酒店id
        :return: 房间列表
        """
        with create_db_session() as session:
            statement = (
                select(HotelRoom)
                .where(HotelRoom.hotel_id == hotel_id)
                .order_by(HotelRoom.no)
            )
            return session.exec(statement).all()