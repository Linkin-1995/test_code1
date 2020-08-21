"""
    练习:参照day03/exercise05案例,
        定义函数,根据课程编号计算课程名称。

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


def get_course_name(course):
    dict_course_infos = {
        "1": "Python语言核心编程",
        "2": "Python高级软件技术",
        "3": "Web 全栈",
        "4": "网络爬虫",
        "5": "数据分析、人工智能",
    }
    if course in dict_course_infos:
        return dict_course_infos[course]
    # return None

print( get_course_name("1"))  # Python语言核心编程
