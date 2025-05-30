from fastapi import APIRouter
from fastapi import Request
from fastapi import Query

from lemon_service.decorator.api import api_need_login
from lemon_service.schema.api import ApiResponse
from lemon_service.schema.hotel import HotelRoomSchema, HotelRoomUseRecordSaveReqSchema
from lemon_service.service.hotel import HotelService

hotel_router = APIRouter(prefix="/hotel", tags=["酒店API"])

hotel_service = HotelService()


@api_need_login
@hotel_router.get("/list-all-hotel", summary="获取所有酒店信息")
async def list_all_hotel(reqeust: Request = None):
    return ApiResponse(
        body=hotel_service.list_all_hotel()
    )


@api_need_login
@hotel_router.get("/list-all-hotel-room-type", summary="获取所有酒店房型信息")
async def list_all_hotel_room_type(reqeust: Request = None):
    return ApiResponse(
        body=hotel_service.list_all_hotel_room_type()
    )


@api_need_login
@hotel_router.put("/save-room", summary="保存房间信息")
async def save_hotel_room(data: HotelRoomSchema, reqeust: Request = None):
    return ApiResponse(
        body=hotel_service.save_hotel_room(data)
    )


@hotel_router.delete("/delete-room", summary="删除房间信息")
# @api_need_login
async def delete_hotel_room(hotel_room_id: str = Query(..., alias="hotelRoomId"), reqeust: Request = None):
    return ApiResponse(
        body=hotel_service.delete_hotel_room(hotel_room_id)
    )


@hotel_router.get("/list-hotel-all-room", summary="获取酒店所有房间信息")
# @api_need_login
async def list_hotel_all_room(hotel_id: str = Query(..., alias="hotelId"), reqeust: Request = None):
    return ApiResponse(
        body=hotel_service.list_hotel_all_room(hotel_id)
    )


@hotel_router.put("/save-room-use-record", summary="保存房间使用记录")
# @api_need_login
async def save_hotel_room_use_record(data: HotelRoomUseRecordSaveReqSchema, reqeust: Request = None):
    return ApiResponse(
        body=hotel_service.save_hotel_room_use_record(data)
    )


@hotel_router.delete("/delete-room-use_-ecord", summary="删除房间使用记录")
# @api_need_login
async def delete_hotel_room_use_record(hotel_room_use_record_id: str = Query(..., alias="hotelRoomUseRecordId"), reqeust: Request = None):
    return ApiResponse(
        body=hotel_service.delete_hotel_room_use_record(hotel_room_use_record_id)
    )


@hotel_router.get("/list-hotel-room-all-use-record", summary="获取房间所有使用记录")
# @api_need_login
async def list_hotel_room_all_use_record(hotel_room_id: str = Query(..., alias="hotelRoomId"), reqeust: Request = None):
    return ApiResponse(
        body=hotel_service.list_hotel_room_all_use_record(hotel_room_id)
    )
