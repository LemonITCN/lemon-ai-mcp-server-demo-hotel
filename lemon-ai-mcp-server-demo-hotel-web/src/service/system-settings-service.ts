import {HttpRequest, HttpUtils} from '@/utils/http-utils.ts'
import type SystemSettingsDto from '@/model/system-settings-dto.ts'

export default class SystemSettingsService {
    public static listAllSettings(): Promise<SystemSettingsDto[]> {
        return new Promise<SystemSettingsDto[]>((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('GET', '/system-settings/list-all'))
                .then((resp) => {
                    resolve(resp.data.body)
                })
                .catch((e) => {
                    reject(new Error(e))
                })
        })
    }

    // 更新设置项
    public static update(settings: SystemSettingsDto): Promise<void> {
        return new Promise((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('PUT', '/system-settings/update').setData(settings))
                .then(() => {
                    resolve()
                })
                .catch((e) => {
                    reject(new Error(e))
                })
        })
    }
}