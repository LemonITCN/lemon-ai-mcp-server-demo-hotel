import {HttpRequest, HttpUtils} from '@/utils/http-utils'
import type HotelDto from '@/model/hotel-dto.ts'
import type HotelRoomTypeDto from '@/model/hotel-room-type-dto'
import type HotelRoomDto from '@/model/hotel-room-dto'

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

    // 获取所有房型
    public static listAllHotelRoomType(): Promise<HotelRoomTypeDto[]> {
        return new Promise((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('GET', '/hotel/list-all-hotel-room-type'))
                .then((res) => {
                    resolve(res.data.body)
                })
                .catch((err) => {
                    reject(err)
                })
        })
    }

    // 获取指定酒店的所有房间
    public static listAllHotelRoom(hotelId: string): Promise<HotelRoomDto[]> {
        return new Promise((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('GET', '/hotel/list-hotel-all-room')
                .setParams({hotelId: hotelId}))
                .then((res) => {
                    resolve(res.data.body)
                })
                .catch((err) => {
                    reject(err)
                })
        })
    }

    // 创建酒店房间
    public static saveHotelRoom(room: HotelRoomDto): Promise<HotelRoomDto> {
        return new Promise((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('PUT', '/hotel/save-room')
                .setData(room))
                .then((res) => {
                    resolve(res.data.body)
                })
                .catch((err) => {
                    reject(err)
                })
        })
    }

    // 删除酒店房间
    public static deleteHotelRoom(roomId: string): Promise<void> {
        return new Promise((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('DELETE', '/hotel/delete-room')
                .setParams({ hotelRoomId: roomId }))
                .then(() => {
                    resolve()
                })
                .catch((err) => {
                    reject(err)
                })
        })
    }
}