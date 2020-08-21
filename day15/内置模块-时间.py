"""
    内置模块 -- 时间
"""
import time

# 1. 生活中的时间 - 从公园元年
#    时间元组：年,月,日,时,分,秒,星期,年的天,夏令时
tuple_time = time.localtime()
print(tuple_time[1]) # 获取月份

# 2. 计算机的时间 - 1970年元旦
#    时间戳：经过的秒数 1595237036.9866097
print(time.time())

# 3. 时间戳 --> 时间元组
# 语法：时间元组 = time.localtime(时间戳)
print(time.localtime(  1595237036.9866097  ))
# (tm_year=2020, tm_mon=7, tm_mday=20, tm_hour=17, tm_min=23, tm_sec=56, tm_wday=0, tm_yday=202, tm_isdst=0)

# 4. 时间元组 --> 时间戳
# 语法：时间戳 = time.mktime(时间元组)
print(time.mktime(tuple_time))

# 5. 时间元组 --> 字符串
# 语法：字符串 = time.strftime("格式",时间元组)
print(time.strftime("%y/%m/%d %H:%M:%S",tuple_time))
# 2020/07/20 17:38:24
print(time.strftime("%Y/%m/%d %H:%M:%S",tuple_time))

# 6. 字符串　 --> 时间元组
print(time.strptime("2020/07/20 17:38:24","%Y/%m/%d %H:%M:%S"))

"""
练习：
    定义函数,根据年月日计算星期数
        参数：年、月、日
        返回值：星期一、　星期二 ....
        思路：根据参数创建时间元组
        　　　通过数据元组获取星期
             星期数改为星期字符串
             0 1     星期一、星期二
"""