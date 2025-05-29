import {HttpRequest, HttpUtils} from '@/utils/http-utils'
import type HotelDto from '@/model/hotel-dto.ts'
import type WordDto from '@/model/word-dto.ts'

export default class MemorizeService {

    public static readonly MEMORIZE_WORD_AUDIO_BASE_URL = 'https://ykmfile.geshuinfo.cn/download/memorize-words/system_word_audio/'

    // 获取书籍列表
    public static getBookList(): Promise<HotelDto[]> {
        return new Promise<HotelDto[]>((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('GET', '/memorize/book-list')).then(res => {
                resolve(res.data.body)
            }).catch(e => {
                reject(e)
            })
        })
    }

    // 获取书籍的所有单词列表
    public static getBookAllWordList(bookDataKey: string): Promise<WordDto[]> {
        return new Promise<WordDto[]>((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('GET', '/memorize/book-word-list').setParams({bookDataKey: bookDataKey}))
                .then(res => {
                    resolve(res.data.body)
                })
                .catch(e => {
                    reject(e)
                })
        })
    }

    // 更新单词
    public static updateWord(wordDto: WordDto): Promise<WordDto> {
        return new Promise<WordDto>((resolve, reject) => {
            HttpUtils.request(HttpRequest.NewInstance('PUT', '/memorize/update-word').setData(wordDto))
                .then(res => {
                    resolve(res.data.body)
                })
                .catch(e => {
                    reject(e)
                })
        })
    }

}