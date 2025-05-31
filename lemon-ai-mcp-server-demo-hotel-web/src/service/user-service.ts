import {HttpRequest, HttpUtils} from '@/utils/http-utils.ts'
import type UserLoginResp from '@/model/user-login-resp.ts'

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

}