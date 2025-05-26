from lemon_service.model.hotel_room import HotelRoom
from lemon_service.repository.hotel import HotelRepository
from lemon_service.schema.hotel import HotelAddRoomAddReq


class HotelService:

    def save_hotel_room(self, hotel_add_room_req: HotelAddRoomAddReq) -> HotelRoom:
        """
        添加 / 更新酒店房间
        :param hotel_add_room_req: 添加酒店房间请求
        :return: 酒店房间对象
        """
        hotel_repository = HotelRepository()
        hotel = hotel_repository.get(hotel_add_room_req.hotel_id)
        if not hotel:
            hotel = HotelRoom()
        hotel.hotel_id = hotel_add_room_req.id
        hotel.hotel_room_type_id = hotel_add_room_req.hotel_room_type_id
        hotel.no = hotel_add_room_req.no
        hotel_repository.upsert(hotel)
        return hotel

    def delete_hotel_room(self, hotel_room_id: str):
        """
        删除酒店房间
        :param hotel_room_id: 酒店房间id
        """
        hotel_repository = HotelRepository()
        hotel_repository.delete(hotel_room_id)
