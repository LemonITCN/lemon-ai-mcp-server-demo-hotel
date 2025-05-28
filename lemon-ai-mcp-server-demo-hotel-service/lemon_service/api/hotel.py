from fastapi import APIRouter
from fastapi import Request

from lemon_service.decorator.api import api_need_login
from lemon_service.schema.hotel import HotelRoomSaveReqSchema, HotelRoomUseRecordSaveReqSchema
from lemon_service.service.hotel import HotelService

hotel_router = APIRouter(prefix="/hotel", tags=["酒店API"])

hotel_service = HotelService()


@api_need_login
@hotel_router.get("/list_all_hotel", summary="获取所有酒店信息")
async def list_all_hotel(reqeust: Request = None):
    return hotel_service.list_all_hotel()


@api_need_login
@hotel_router.get("/list_all_hotel_room_type", summary="获取所有酒店房型信息")
async def list_all_hotel_room_type(reqeust: Request = None):
    return hotel_service.list_all_hotel_room_type()


@api_need_login
@hotel_router.put("/save_room", summary="保存房间信息")
async def save_hotel_room(data: HotelRoomSaveReqSchema, reqeust: Request = None):
    return hotel_service.save_hotel_room(data)


@hotel_router.delete("/delete_room", summary="删除房间信息")
# @api_need_login
async def delete_hotel_room(hotel_room_id: str, reqeust: Request = None):
    return hotel_service.delete_hotel_room(hotel_room_id)


@hotel_router.get("/list_hotel_all_room", summary="获取酒店所有房间信息")
# @api_need_login
async def list_hotel_all_room(hotel_id: str, reqeust: Request = None):
    return hotel_service.list_hotel_all_room(hotel_id)


@hotel_router.put("/save_room_use_record", summary="保存房间使用记录")
# @api_need_login
async def save_hotel_room_use_record(data: HotelRoomUseRecordSaveReqSchema, reqeust: Request = None):
    return hotel_service.save_hotel_room_use_record(data)


@hotel_router.delete("/delete_room_use_record", summary="删除房间使用记录")
# @api_need_login
async def delete_hotel_room_use_record(hotel_room_use_record_id: str, reqeust: Request = None):
    return hotel_service.delete_hotel_room_use_record(hotel_room_use_record_id)


@hotel_router.get("/list_hotel_room_all_use_record", summary="获取房间所有使用记录")
# @api_need_login
async def list_hotel_room_all_use_record(hotel_room_id: str, reqeust: Request = None):
    return hotel_service.list_hotel_room_all_use_record(hotel_room_id)
