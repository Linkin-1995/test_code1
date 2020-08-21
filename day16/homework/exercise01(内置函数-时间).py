import time


def get_week(year, month, day):
    # str_time = f"{year}-{month}-{day}"
    # 字符串%(变量)
    str_time = "%d-%d-%d" % (year, month, day)
    # 时间元组 = time.strptime(字符串,格式)
    #                ("2020-7-21","%Y-%m-%d")
    tuple_time = time.strptime(str_time, "%Y-%m-%d")
    week_index = tuple_time[6]
    weeks = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return weeks[week_index]


print(get_week(2020, 7, 21))
