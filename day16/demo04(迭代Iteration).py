"""
    迭代Iteration:依次获取容器每个元素
    可迭代对象iterable:能够返回迭代器
    迭代器iterator:做迭代的工具
"""
message = "我是齐天大圣孙悟空"
# for item in message:
#     print(item)

# for 循环原理
"""
    练习1: 用迭代思想,获取列表中所有元素
    练习2: 用迭代思想,获取字典中所有元素 
"""
# 1. 获取迭代器对象
iterator = message.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
        # 3. 停止循环获取
    except StopIteration:
        break
# 笔试题:能够参与for循环的条件是什么?
# 答: 对象能够获取迭代器对象( 对象具有__iter__函数 )

# 机试题:不过for循环,获取字典所有键值对.
dict01 = {"a": "A", "b": "B", "c": "C"}











