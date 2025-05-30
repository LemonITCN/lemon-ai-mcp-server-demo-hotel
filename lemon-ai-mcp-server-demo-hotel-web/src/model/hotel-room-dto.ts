import BaseEntityDto from '@/model/base-entity-dto'

export default class HotelRoomDto extends BaseEntityDto {
    // 房间编号
    no = ''
    // 酒店ID
    hotelId = ''
    // 酒店房间类型ID
    hotelRoomTypeId = ''
}