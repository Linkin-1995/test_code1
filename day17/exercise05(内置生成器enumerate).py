# 练习1: 将列表中所有偶数设置为0

list01 = [43, 6, 65, 67, 78, 98]

for i, item in enumerate(list01):
    if item % 2 == 0:
        list01[i] = 0
print(list01)

# 练习2: 遍历字典键值对的同时打印索引
# {"a":"A"}  --> 0  a  A
dict01 = {"a": "A", "b": "B"}
# for i, key, value in enumerate(dict01.items()):
#     print(i, key, value)
# (0, ('a', 'A'))
for i, (key, value) in enumerate(dict01.items()):
    print(i, key, value)
