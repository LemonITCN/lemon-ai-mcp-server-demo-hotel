from datetime import datetime
from typing import List

from lemon_service.schema.hotel import HotelRoomTypeStateSchema
from lemon_service.service.hotel import HotelService
from . import mcp

__hotel_service = HotelService()


@mcp.tool(name="list_all_hotel", description="列出所有酒店门店")
def list_all_hotel() -> List[mcp.Hotel]:
    """
    列出所有酒店
    :return: 酒店列表
    """
    return __hotel_service.list_all_hotel()


@mcp.tool(name="query_hotel_room_state", description="查询酒店每一种房间类型的剩余房间状态及数量")
def query_hotel_room_state(hotel_id: str, query_start_date: str, query_end_date: str) -> List[HotelRoomTypeStateSchema]:
    """
    查询指定酒店指定日期范围内房间状
    :param hotel_id: 酒店id
    :param query_start_date: 要查询的开始日期 yyyy-MM-dd
    :param query_end_date: 要查询的结束日期 yyyy-MM-dd
    :return: 房间剩余情况状态
    """
    start_datetime = datetime.strptime(query_start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(query_end_date, "%Y-%m-%d")
    return __hotel_service.query_hotel_room_state(hotel_id, start_datetime, end_datetime)
