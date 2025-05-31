import BaseEntityDto from '@/model/base-entity-dto'

export default class HotelRoomUseRecordDto extends BaseEntityDto {
    // 酒店ID
    hotel_id = ''
    // 酒店房间ID
    hotel_room_id = ''
    // 客人姓名
    client_name = ''
    // 入住开始日期
    use_start_date = 0
    // 入住结束日期
    use_end_date = 0
    // 订单ID
    order_id = ''
}