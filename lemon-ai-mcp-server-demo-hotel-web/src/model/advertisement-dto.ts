import BaseEntityDto from '@/model/base-entity-dto'

export default class AdvertisementDto extends BaseEntityDto {
    // 标题
    title = ''
    // 图片URL
    imageUrl = ''
    // 跳转URL
    linkUrl = ''
    // 频道，home首页、class方法课、mine我的
    channel = ''
    // 排序编号
    sort = 0
}