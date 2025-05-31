from datetime import datetime


def get_current_datetime_str_cn() -> str:
    """
    获取当前日期时间的中文描述字符串
    :return:  日期字符串
    """
    # 中文星期映射
    weekday_map = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

    now = datetime.now()
    date_str = now.strftime("%Y年%m月%d日")
    time_str = now.strftime("%H:%M:%S")
    weekday_str = weekday_map[now.weekday()]

    return f"{date_str} {time_str} {weekday_str}"
