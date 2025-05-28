import type {AdcTimeUnitType} from '@/model/analytics/dashboard-component/adc-base-type'

export default class DateUtils {
  public static format(date: Date, fmt: string) {
    const o: any = {
      'M+': date.getMonth() + 1,
      'd+': date.getDate(),
      'h+': date.getHours(),
      'm+': date.getMinutes(),
      's+': date.getSeconds(),
      'q+': Math.floor((date.getMonth() + 3) / 3),
      S: date.getMilliseconds()
    }
    if (/(y+)/.test(fmt)) {
      fmt = fmt.replace(RegExp.$1, (date.getFullYear() + '').substr(4 - RegExp.$1.length))
    }
    for (const k in o) {
      if (new RegExp('(' + k + ')').test(fmt)) {
        fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? (o[k]) : (('00' + o[k]).substr(('' + o[k]).length)))
      }
    }
    return fmt
  }

  public static utcFormat(date: Date, fmt: string) {
    const o: any = {
      'M+': date.getUTCMonth() + 1,
      'd+': date.getUTCDate(),
      'h+': date.getUTCHours(),
      'm+': date.getUTCMinutes(),
      's+': date.getUTCSeconds(),
      'q+': Math.floor((date.getMonth() + 3) / 3),
      S: date.getUTCMilliseconds()
    }
    if (/(y+)/.test(fmt)) {
      fmt = fmt.replace(RegExp.$1, (date.getUTCFullYear() + '').substr(4 - RegExp.$1.length))
    }
    for (const k in o) {
      if (new RegExp('(' + k + ')').test(fmt)) {
        fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? (o[k]) : (('00' + o[k]).substr(('' + o[k]).length)))
      }
    }
    return fmt
  }

  public static formatByUnit(date: Date, uni: AdcTimeUnitType) {
    const fmt = {
      minute: 'yyyy-MM-dd hh:mm',
      hour: 'yyyy-MM-dd hh',
      day: 'yyyy-MM-dd',
      month: 'yyyy-MM',
      year: 'yyyy'
    }
    return DateUtils.format(date, fmt[uni])
  }
}
