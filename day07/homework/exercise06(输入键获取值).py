"""
    使用容器思想改写下列代码
    course = input("请输入课程阶段数：")
    if course == "1":
        print("Python语言核心编程")
    elif course == "2":
        print("Python高级软件技术")
    elif course == "3":
        print("Web 全栈")
    elif course == "4":
        print("网络爬虫")
    elif course == "5":
        print("数据分析、人工智能")
"""
course = input("请输入课程阶段数：")
dict_course_infos = {
    "1": "Python语言核心编程",
    "2": "Python高级软件技术",
    "3": "Web 全栈",
    "4": "网络爬虫",
    "5": "数据分析、人工智能",
}
# 如果键存在,就获取值(如果不判断,可能报错)
if course in dict_course_infos:
    print(dict_course_infos[course])
