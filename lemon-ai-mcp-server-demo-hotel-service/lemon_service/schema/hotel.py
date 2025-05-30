from lemon_service.base import LemonBaseSchema


class HotelRoomSchema(LemonBaseSchema):
    """
    创建房间
    """
    id: str
    no: str
    hotelId: str
    hotelRoomTypeId: str


class HotelRoomUseRecordSaveReqSchema(LemonBaseSchema):
    """
    添加房间入住/预约记录
    """
    id: str
    hotel_room_id: str
    client_name: str
    # unix时间戳 精确到毫秒
    use_start_date: int
    use_end_date: int


class HotelRoomTypeStateSchema(LemonBaseSchema):
    """
    房间类型状态
    """
    #  酒店名称
    hotel_name: str
    # 房间类型id
    hotel_room_type_id: str
    # 房间类型名称
    hotel_room_type_name: str
    # 剩余数量
    balance_count: int
