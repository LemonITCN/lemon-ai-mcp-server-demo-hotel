import {HttpRequest, HttpUtils} from '@/utils/http-utils'
import type HotelDto from '@/model/hotel-dto.ts'

export default class HotelService {

    // 获取所有酒店
    public static listAllHotel(): Promise<HotelDto[]> {
        return new Promise((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('GET', '/hotel/list-all-hotel'))
                .then((res) => {
                    resolve(res.data.body)
                })
                .catch((err) => {
                    reject(err)
                })
        })
    }

}