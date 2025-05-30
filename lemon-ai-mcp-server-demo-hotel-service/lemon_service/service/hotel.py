from datetime import datetime
from typing import List

from lemon_service.model.hotel import Hotel
from lemon_service.model.hotel_room import HotelRoom
from lemon_service.model.hotel_room_type import HotelRoomType
from lemon_service.model.hotel_room_use_record import HotelRoomUseRecord
from lemon_service.repository import HotelRepository
from lemon_service.repository import HotelRoomRepository, HotelRoomUseRecordRepository
from lemon_service.repository import HotelRoomTypeRepository
from lemon_service.schema.hotel import HotelRoomSchema, HotelRoomUseRecordSaveReqSchema
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

    def save_hotel_room(self, hotel_room_save_req: HotelRoomSchema) -> HotelRoom:
        """
        添加 / 更新酒店房间
        :param hotel_room_save_req: 保存酒店房间请求
        :return: 酒店房间对象
        """
        hotel_room = self.__hotel_room_repository.get(hotel_room_save_req.id)
        if not hotel_room:
            hotel_room = HotelRoom()
        hotel_room.hotel_id = hotel_room_save_req.hotelId
        hotel_room.hotel_room_type_id = hotel_room_save_req.hotelRoomTypeId
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
        room_model_list = self.__hotel_room_repository.list_hotel_all_room(hotel_id)
        # 转换成schema list
        room_schema_list = []
        for room_model in room_model_list:
            room_schema = HotelRoomSchema(
                hotelId=room_model.hotel_id,
                hotelRoomTypeId=room_model.hotel_room_type_id,
                no=room_model.no,
                id=room_model.id,
            )
            room_schema_list.append(room_schema)
        return room_schema_list

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
        # 获取酒店对象
        hotel = self.__hotel_repository.get(hotel_id)
        # 先列出指定酒店每种房型的房间数量
        every_type_room_count_pool = self.__hotel_room_type_repository.count_every_hotel_room_type_room_count(hotel_id)
        # 然后统计指定时间端内指定酒店的所有房间使用记录
        in_time_range_use_record_list = self.__hotel_room_use_record_repository.list_hotel_time_range_all_use_record(
            hotel_id=hotel_id, query_start_date=query_start_date, query_end_date=query_end_date
        )
        for use_record in in_time_range_use_record_list:
            # 遍历咩一条 使用记录，然后给房间数量-1
            every_type_room_count_pool[use_record.hotel_room_type_id] -= 1
        # 获取所有房型
        hotel_room_type_list = self.__hotel_room_type_repository.list_all()
        room_type_state_list = []
        for hotel_room_type in hotel_room_type_list:
            if hotel_room_type.id not in every_type_room_count_pool:
                every_type_room_count_pool[hotel_room_type.id] = 0
            room_type_state = HotelRoomTypeStateSchema(
                hotelId=hotel_id,
                hotelName=hotel.name,
                hotelRoomTypeId=hotel_room_type.id,
                hotelRoomTypeName=hotel_room_type.name,
                balanceCount=every_type_room_count_pool[hotel_room_type.id],
            )
            room_type_state_list.append(room_type_state)
        return room_type_state_list
