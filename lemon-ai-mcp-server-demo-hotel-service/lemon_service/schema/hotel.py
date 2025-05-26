from pydantic import BaseModel


class HotelAddRoomAddReq(BaseModel):
    """
    创建房间
    """
    id: str
    no: str
    hotel_id: str
    hotel_room_type_id: str
