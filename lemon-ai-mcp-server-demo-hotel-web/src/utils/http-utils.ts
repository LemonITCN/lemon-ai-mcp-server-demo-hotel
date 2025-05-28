import axios, {type AxiosRequestConfig, type AxiosResponse, type Method} from 'axios'

class HttpRequest {
    method: Method = 'GET'
    url = ''
    data: any = {}
    params: { [index: string]: any } = {}
    header: { [index: string]: string } | undefined
    readonly clientTimestamp = new Date().getTime()
    isDownload = false

    public static NewInstance(method: Method, url: string): HttpRequest {
        const instance: HttpRequest = new HttpRequest()
        instance.method = method
        instance.url = url
        return instance
    }

    setData(data: any): HttpRequest {
        this.data = data
        return this
    }

    setParams(params: any): HttpRequest {
        this.params = params
        return this
    }

    setHeader(header: { [index: string]: string }): HttpRequest {
        this.header = header
        return this
    }

    setIsDownload(isDownload: boolean): HttpRequest {
        this.isDownload = isDownload
        return this
    }
}

class HttpResponse {
    data: any = {}
    statusCode = 0
    header: any = {}
    cookies: string[] = []
}

class HttpUtils {

    private static readonly _DEFAULT_TIMEOUT = 60000
    private static _defaultHeader: { [index: string]: string } = {}

    public static set defaultHeader(value: { [p: string]: string }) {
        this._defaultHeader = value
    }

    public static get defaultHeader(): { [p: string]: string } {
        const defaultHeader: { [p: string]: string } = Object.assign({}, this._defaultHeader)
        return defaultHeader
    }

    public static addDefaultHeader(key: string, value: string) {
        this._defaultHeader[key] = value
    }

    public static removeDefaultHeader(key: string) {
        delete this._defaultHeader[key]
    }

    public static getBaeUrl() {
        return 'http://localhost:23232'
    }

    public static request(options: HttpRequest): Promise<HttpResponse> {
        return new Promise<HttpResponse>((resolve, reject) => {
            if (options.header === undefined) {
                options.header = {}
            }
            for (const defaultHeaderKey in this._defaultHeader) {
                options.header[defaultHeaderKey] = this._defaultHeader[defaultHeaderKey]
            }
            const url = (options.url.startsWith('http') ? '' : this.getBaeUrl()) + options.url
            let endUrl = ''
            Object.keys(options.params).forEach((paramKey: string) => {
                if (endUrl !== '') {
                    endUrl += '&'
                }
                endUrl += paramKey + '=' + options.params[paramKey]
            })
            // @ts-ignore
            const requestObject: AxiosRequestConfig = {
                url: url + (url.indexOf('?') >= 0 ? '&' : '?') + endUrl,
                method: options.method,
                data: options.data,
                timeout: this._DEFAULT_TIMEOUT,
                responseType: options.isDownload ? 'blob' : 'json',
                headers: options.header
            }
            axios.request(requestObject)
                .then((resp: AxiosResponse) => {
                    if (resp.status >= 200 && resp.status < 300) {
                        const response = new HttpResponse()
                        response.data = resp.data
                        response.header = resp.headers
                        response.statusCode = resp.status
                        resolve(response)
                    } else {
                        if (resp.status === 401) {
                            HttpUtils.show401ErrorMessage()
                            location.href = '#/login'
                        }
                        reject(new Error(resp.data.message))
                    }
                })
                .catch((e: any) => {
                    if (e.response.status === 401) {
                        HttpUtils.show401ErrorMessage()
                        location.href = '#/login'
                    }
                    try {
                        if (e.response.data.errCode === 'USER_TOKEN_EXPIRED') {
                            HttpUtils.show401ErrorMessage()
                        } else {
                            reject(new Error(e.response.data.errCode))
                        }
                    } catch (e) {
                        console.error('HTTP-UTILS ERROR:', e)
                        reject(new Error('unknown error'))
                    }
                })
        })
    }

    private static lastShow401ErrorAt = 0

    public static show401ErrorMessage() {
        const now = new Date().getTime()
        if ((now - this.lastShow401ErrorAt) > 2000) {
            HttpUtils.lastShow401ErrorAt = now
        }
    }
}

export {
    HttpRequest,
    HttpResponse,
    HttpUtils
}
