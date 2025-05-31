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
    hotelRoomId: str
    clientName: str
    # unix时间戳 精确到毫秒
    useStartDate: int
    useEndDate: int


class HotelRoomTypeStateSchema(LemonBaseSchema):
    """
    房间类型状态
    """
    # 酒店id
    hotelId: str
    #  酒店名称
    hotelName: str
    # 房间类型id
    hotelRoomTypeId: str
    # 房间类型名称
    hotelRoomTypeName: str
    # 剩余数量
    balanceCount: int
