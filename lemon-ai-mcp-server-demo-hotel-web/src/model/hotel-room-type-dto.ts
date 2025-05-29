import BaseEntityDto from '@/model/base-entity-dto'

export default class HotelRoomTypeDto extends BaseEntityDto {
    // 酒店房间类型
    name = ''
    // 可入住人数
    people_count = ''
    // 房间类型介绍
    description = ''
    // 房间价格,单位元
    price = 0
}