import BaseEntityDto from '@/model/base-entity-dto'

export default class OrderDto extends BaseEntityDto {
    // 订单编号
    no = ''
    // 酒店ID
    hotel_id = ''
    // 订单总价格
    total_price = 0
    // 支付状态，是否已经支付
    pay_state = false
}