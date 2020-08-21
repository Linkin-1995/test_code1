# 用迭代思想,获取字典中所有元素
dict01 = {"a": "A", "b": "B", "c": "C"}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, dict01[key])
    except StopIteration:
        break
