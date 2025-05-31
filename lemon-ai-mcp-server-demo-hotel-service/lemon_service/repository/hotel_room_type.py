from sqlmodel import select, func

from lemon_service.base.base_repository import BaseRepository
from lemon_service.core.db_engine import create_db_session
from lemon_service.model import HotelRoomType, HotelRoom


class HotelRoomTypeRepository(BaseRepository[HotelRoomType]):
    """
    酒店房间 数据访问
    """

    def __init__(self):
        super().__init__(HotelRoomType)

    def count_every_hotel_room_type_room_count(self, hotel_id: str):
        """
        统计指定酒店每种房型的房间数量
        :param hotel_id: 酒店id
        :return:
        """
        with create_db_session() as session:
            statement = (
                select(HotelRoom.hotel_room_type_id, func.count().label("room_count"))
                .where(HotelRoom.hotel_id == hotel_id)
                .group_by(HotelRoom.hotel_room_type_id)
            )

            results = session.exec(statement).all()

            # 构建结果字典
            return {room_type_id: count for room_type_id, count in results}
