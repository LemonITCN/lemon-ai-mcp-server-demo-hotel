import BaseEntityDto from '@/model/base-entity-dto.ts'

export default class UserDto extends BaseEntityDto{
    // 用户主键
    dataKey = ''
    // 昵称
    nickname = ''
    // 手机号码
    phone = ''
    // 头像URL
    avatarUrl = ''
    // VIP充值时间
    vipRechargeTime = 0
    // 自动播放时间，单位秒
    autoPlaySeconds = 0
    // 自动播放次数
    autoPlayCount = 0
}