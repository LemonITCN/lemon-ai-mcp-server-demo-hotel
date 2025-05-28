import {HttpRequest, HttpUtils} from '@/utils/http-utils'
import type AdvertisementDto from '@/model/advertisement-dto'

export default class AdvertisementService {

    // 通过频道获取广告列表
    public static getAdvertisementListByChannel(channel: string): Promise<AdvertisementDto[]> {
        return new Promise((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('GET', '/advertisement/list-by-channel').setParams({channel}))
                .then((res) => {
                    resolve(res.data.body)
                })
                .catch((err) => {
                    reject(err)
                })
        })
    }

    // 更新广告
    public static updateAdvertisement(advertisement: AdvertisementDto): Promise<AdvertisementDto> {
        return new Promise((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('PUT', '/advertisement/update').setData(advertisement))
                .then((res) => {
                    resolve(res.data.body)
                })
                .catch((err) => {
                    reject(err)
                })
        })
    }

    // 删除广告
    public static deleteAdvertisement(dataKey: string): Promise<void> {
        return new Promise((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('DELETE', '/advertisement/delete').setParams({dataKey}))
                .then((res) => {
                    resolve()
                })
                .catch((err) => {
                    reject(err)
                })
        })
    }

    // 更新广告排序
    public static updateSort(advertisementDataKeyList: string[], channel: string): Promise<void> {
        return new Promise((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('PUT', '/advertisement/update-sort').setData({
                advertisementDataKeyList,
                channel
            })).then((res) => {
                resolve()
            }).catch((err) => {
                reject(err)
            })
        })
    }
}