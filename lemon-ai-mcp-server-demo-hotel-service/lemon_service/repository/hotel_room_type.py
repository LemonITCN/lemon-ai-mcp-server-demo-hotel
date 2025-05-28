from sqlmodel import select, func

from lemon_service.base.base_repository import BaseRepository
from lemon_service.core.db_engine import create_db_session
from lemon_service.model import HotelRoomType, HotelRoom, HotelRoomUseRecord


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
            stmt = (
                select(
                    HotelRoom.hotel_room_type_id,
                    func.count().label("room_count"),
                    HotelRoomType.name,
                    HotelRoomType.people_count,
                    HotelRoomType.description
                )
                .join(HotelRoomType, HotelRoomType.id == HotelRoom.hotel_room_type_id)
                .where(HotelRoom.hotel_id == hotel_id)
                .group_by(
                    HotelRoom.hotel_room_type_id,
                )
            )
            results = session.exec(stmt).all()
            return results

    def count_hotel_room_room_type_used_record_count(self, hotel_id: str):
        """
        统计指定酒店每种房型的入住记录数量
        :param hotel_id: 酒店id
        :return:
        """
        with create_db_session() as session:
            stmt = (
                select(
                    HotelRoomUseRecord.hotel_room_id,
                    HotelRoom.hotel_room_type_id,
                    func.count().label("used_record_count"),
                    HotelRoomType.name,
                    HotelRoomType.people_count,
                    HotelRoomType.description
                )
                .join(HotelRoom, HotelRoom.id == HotelRoomUseRecord.hotel_room_id)
                .join(HotelRoomType, HotelRoomType.id == HotelRoom.hotel_room_type_id)
                .where(HotelRoom.hotel_id == hotel_id)
                .group_by(
                    HotelRoom.hotel_room_type_id,
                )
            )
            results = session.exec(stmt).all()
            return results
