from datetime import datetime
from typing import List

from lemon_service.model.hotel import Hotel
from lemon_service.model.hotel_room import HotelRoom
from lemon_service.model.hotel_room_type import HotelRoomType
from lemon_service.model.hotel_room_use_record import HotelRoomUseRecord
from lemon_service.repository import HotelRepository
from lemon_service.repository import HotelRoomRepository, HotelRoomUseRecordRepository
from lemon_service.repository import HotelRoomTypeRepository
from lemon_service.schema.hotel import HotelRoomSaveReqSchema, HotelRoomUseRecordSaveReqSchema
from lemon_service.schema.hotel import HotelRoomTypeStateSchema


class HotelService:
    __hotel_repository = HotelRepository()
    __hotel_room_repository = HotelRoomRepository()
    __hotel_room_type_repository = HotelRoomTypeRepository()
    __hotel_room_use_record_repository = HotelRoomUseRecordRepository()

    def list_all_hotel(self) -> List[Hotel]:
        """
        获取所有的酒店列表
        :return: 酒店列表
        """
        return self.__hotel_repository.list_all()

    def list_all_hotel_room_type(self) -> List[HotelRoomType]:
        """
        获取所有酒店房型列表
        :return: 酒店房型列表
        """
        return self.__hotel_room_type_repository.list_all()

    def save_hotel_room(self, hotel_room_save_req: HotelRoomSaveReqSchema) -> HotelRoom:
        """
        添加 / 更新酒店房间
        :param hotel_room_save_req: 保存酒店房间请求
        :return: 酒店房间对象
        """
        hotel_room = self.__hotel_room_repository.get(hotel_room_save_req.hotel_id)
        if not hotel_room:
            hotel_room = HotelRoom()
        hotel_room.hotel_id = hotel_room_save_req.id
        hotel_room.hotel_room_type_id = hotel_room_save_req.hotel_room_type_id
        hotel_room.no = hotel_room_save_req.no
        self.__hotel_room_repository.upsert(hotel_room)
        return hotel_room

    def delete_hotel_room(self, hotel_room_id: str):
        """
        删除酒店房间
        :param hotel_room_id: 酒店房间id
        """
        self.__hotel_room_repository.delete(hotel_room_id)

    def list_hotel_all_room(self, hotel_id: str):
        """
        获取所有酒店房间列表
        :param hotel_id: 酒店id
        :return: 酒店房间列表
        """
        return self.__hotel_room_repository.list_hotel_all_room(hotel_id)

    def save_hotel_room_use_record(self,
                                   hotel_room_use_record_save_req: HotelRoomUseRecordSaveReqSchema) -> HotelRoomUseRecord:
        """
        添加 / 更新酒店使用记录
        :param hotel_room_use_record_save_req:
        :return:
        """

        hotel_room_repository = HotelRoomRepository()
        hotel_room_use_record = self.__hotel_room_use_record_repository.get(hotel_room_use_record_save_req.id)
        if not hotel_room_use_record:
            hotel_room_use_record = HotelRoomUseRecord()
        hotel_room = hotel_room_repository.get(hotel_room_use_record_save_req.hotel_room_id)
        hotel_room_use_record.hotel_id = hotel_room.hotel_id
        hotel_room_use_record.hotel_room_id = hotel_room_use_record_save_req.hotel_room_id
        hotel_room_use_record.client_name = hotel_room_use_record_save_req.client_name
        hotel_room_use_record.use_start_date = datetime.fromtimestamp(
            hotel_room_use_record_save_req.use_start_date / 1000)
        hotel_room_use_record.use_end_date = datetime.fromtimestamp(hotel_room_use_record_save_req.use_end_date / 1000)
        return hotel_room_use_record

    def delete_hotel_room_use_record(self, hotel_room_use_record_id: str):
        """
        删除酒店使用记录
        :param hotel_room_use_record_id:
        """
        self.__hotel_room_use_record_repository.delete(hotel_room_use_record_id)

    def list_hotel_room_all_use_record(self, hotel_room_id: str):
        """
        获取所有酒店房间使用记录列表
        :param hotel_room_id: 酒店房间id
        :return: 酒店房间入住、预约记录
        """
        return self.__hotel_room_use_record_repository.list_hotel_room_all_use_record(hotel_room_id)

    def query_hotel_room_state(self, hotel_id: str, query_start_date: datetime, query_end_date: datetime) -> List[
        HotelRoomTypeStateSchema]:
        """
        查询指定酒店指定日期范围内房间状态
        :param hotel_id: 酒店id
        :param query_start_date: 查询的开始日期
        :param query_end_date: 查询的结束如期
        :return:
        """
        pass
