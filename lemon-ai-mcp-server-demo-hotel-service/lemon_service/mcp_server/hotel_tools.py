from datetime import datetime
from typing import List

from lemon_service.model.hotel import Hotel
from lemon_service.model.hotel_room_type import HotelRoomType
from lemon_service.schema.hotel import HotelRoomTypeStateSchema
from lemon_service.service.hotel import HotelService

__hotel_service = HotelService()


def register_all_hotel_tools(mcp):
    """
    注册酒店tools
    :param mcp: mcp对象
    """

    @mcp.tool(name="list_all_hotel", description="列出所有酒店门店，返回包含门店的地址和名称")
    def list_all_hotel() -> List[Hotel]:
        """
        列出所有酒店
        :return: 酒店列表
        """
        all_hotel_list = __hotel_service.list_all_hotel()
        return all_hotel_list

    @mcp.tool(name="list_all_hotel_room_type",
              description="列出所有房间类型，返回每种房型的简介、名称、可住人数和价格，所有门店的房型都是通用的，即获取到的房型每个门店都是这些")
    def list_all_hotel_room_type() -> List[HotelRoomType]:
        """
        列出所有酒店门店
        :return: 酒店列表
        """
        all_hotel_room_type_list = __hotel_service.list_all_hotel_room_type()
        return all_hotel_room_type_list

    @mcp.tool(name="query_hotel_room_state",
              description="查询某个门店在某段时间内每一种房间类型的剩余房间状态及数量，需要传入酒店的id(hotel_id)，以及开始时间(query_start_date)和结束时间(query_end_date),开始时间和结束时间传的是日期字符串，格式是:yyyy-MM-dd")
    def query_hotel_room_state(hotel_id: str, query_start_date: str, query_end_date: str) -> List[
        HotelRoomTypeStateSchema]:
        """
        查询指定酒店指定日期范围内房间状
        :param hotel_id: 酒店id
        :param query_start_date: 要查询的开始日期 yyyy-MM-dd
        :param query_end_date: 要查询的结束日期 yyyy-MM-dd
        :return: 房间剩余情况状态
        """
        start_datetime = datetime.strptime(query_start_date, "%Y-%m-%d")
        end_datetime = datetime.strptime(query_end_date, "%Y-%m-%d")
        result = __hotel_service.query_hotel_room_state(hotel_id, start_datetime, end_datetime)
        return result
