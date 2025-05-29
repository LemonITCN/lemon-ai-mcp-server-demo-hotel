import BaseEntityDto from '@/model/base-entity-dto'

export default class HotelRoomDto extends BaseEntityDto {
    // 房间编号
    no = ''
    // 酒店ID
    hotel_id = ''
    // 酒店房间类型ID
    hotel_room_type_id = ''
}