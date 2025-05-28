import type WordDto from '@/model/word-dto'
import BaseEntityDto from '@/model/base-entity-dto'

export default class BookDto extends BaseEntityDto {
    // 书籍名称
    name = ''
    // 书籍唯一键
    key = ''
    // 书籍音频目录名称
    audioDirName = ''
    // 是否包含音频
    hasAudio = false
    // 是否需要VIP
    needVip = true
    // 数据1名称
    data1Name = ''
    // 数据1的样式
    data1Style = ''
    // 数据1在复习时是否显示
    data1ShowInReview = false
    // 数据2名称
    data2Name = ''
    // 数据2的样式
    data2Style = ''
    // 数据2在复习时是否显示
    data2ShowInReview = false
    // 数据3名称
    data3Name = ''
    // 数据3的样式
    data3Style = ''
    // 数据3在复习时是否显示
    data3ShowInReview = false
    // 数据4名称
    data4Name = ''
    // 数据4的样式
    data4Style = ''
    // 数据4在复习时是否显示
    data4ShowInReview = false
    // 数据5名称
    data5Name = ''
    // 数据5的样式
    data5Style = ''
    // 数据5在复习时是否显示
    data5ShowInReview = false
    // 排序
    sort = 0

    // 所有的单词列表
    wordList: WordDto[] = []
}