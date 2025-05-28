import type UserLoginResp from '@/model/user-login-resp.ts'
import {HttpRequest, HttpUtils} from '@/utils/http-utils.ts'
import type UserDto from '@/model/user-dto.ts'
import {DataStore} from '@/stores/data-store.ts'

export default class UserService {


    public static login(number: string, password: string): Promise<UserLoginResp> {
        return new Promise<UserLoginResp>((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('POST', '/user/login').setData({
                number: number,
                password: password
            })).then((resp) => {
                resolve(resp.data.body)
            }).catch((e) => {
                reject(new Error(e))
            })
        })
    }

    // 获取当前用户信息
    public static getCurrentUserInfo(): Promise<UserDto> {
        return new Promise((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('GET', '/user/info'))
                .then((res) => {
                    const userInfo = res.data.body as UserDto
                    if (!userInfo.autoPlayCount) {
                        userInfo.autoPlayCount = 1
                    }
                    if (!userInfo.autoPlaySeconds) {
                        userInfo.autoPlaySeconds = 20
                    }
                    DataStore().setUserInfo(userInfo)
                    resolve(userInfo)
                })
                .catch((err) => {
                    reject(err)
                })
        })
    }

    // 获取所有用户列表
    public static listAllUser(): Promise<UserDto[]> {
        return new Promise((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('GET', '/user/all-user'))
                .then((res) => {
                    resolve(res.data.body)
                })
                .catch((err) => {
                    reject(err)
                })
        })
    }
}