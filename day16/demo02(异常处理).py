"""
    异常处理
        价值：保障程序按照既定流程执行
        适用性：
            不是解决语法错误,
            是运行时逻辑错误(某些数据超过范围)
        现象：不再向下执行,不断向上返回
        处理目的：将异常现象改为正常现象(向下执行)
        处理手段：
            try:
                可能触发异常的语句
            except 错误类型1：
                处理语句1
            except 错误类型2：
                处理语句2
            except Exception：
                不是以上错误类型的处理语句
            else:
                未发生异常的语句
            finally:
                无论是否发生异常的语句

    练习2:对学生信息管理系统进行异常处理
        　体会：保障程序按照既定流程执行
               (正确输入后的数据,不因为其他错误而重写录入)
"""
"""
# 存在异常的代码
def div_apple(apple_count):
    # ValueError
    person_count = int(input("请输入人数："))
    # ZeroDivisionError
    result = apple_count / person_count
    # print("%d个人分得%d个苹果"%(person_count,result))
    print(f"{person_count}个人分得{result}个苹果")

def main():
    div_apple(10)


main()
"""


# 写法1:起死回生(最常用)
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数："))
        result = apple_count / person_count
        print(f"{person_count}个人分得{result}个苹果")
    # except Exception:
    except:
        print("程序出错啦")

# 写法2:对症下药(官方建议)
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数："))
#         result = apple_count / person_count
#         print(f"{person_count}个人分得{result}个苹果")
#     except ValueError:
#         print("输入的不是整数")
#     except ZeroDivisionError:
#         print("输入的是零")


# 写法3:无论对错,最终一定执行
# def div_apple(apple_count):
#     try:
#         # 对文件操作 打开 -死了-> 关闭(finally)
#         person_count = int(input("请输入人数："))
#         result = apple_count / person_count
#         print(f"{person_count}个人分得{result}个苹果")
#     finally:# 无论对错,最终一定执行
#         print("分苹果结束")

# 4. 没有错误执行的逻辑
# def div_apple(apple_count):
#     try:# (尝试执行)
#         # 对文件操作 打开 -死了-> 关闭(finally)
#         person_count = int(input("请输入人数："))
#         result = apple_count / person_count
#         print(f"{person_count}个人分得{result}个苹果")
#     except Exception:
#         print("有错误")
#     else:# 没错误
#         print("分苹果成功")


div_apple(10)

print("后续逻辑")
