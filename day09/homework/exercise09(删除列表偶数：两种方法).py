"""
11. (选做)定义函数,将数字列表中所有偶数删除.
    list01 = [4,55,6,78,66,22,89,90]
             [55,89]
    提示:有坑,需谨慎(调试).
"""


# 需求:在列表中删除多个元素
# 缺点:漏删(后面元素向前移动)
#      报错(元素不足)
# def delete_all_even(list_target):
#     for i in range(len(list_target)):
#         if list_target[i] % 2 == 0:
#              del list_target[i]

# 解决:倒序删除(删除元素不会影响即将判断的元素)
def delete_all_even(list_target):
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] % 2 == 0:
            del list_target[i]


list01 = [4, 55, 6, 78, 66, 22, 89, 90]
delete_all_even(list01)
print(list01)

或者
list01 = [4,55,6,78,66,22,89,90]
def delete_an_even_number(list):
    index=0
    for i in range(len(list)):
        if list[i]%2!=0:
            list[index]=list[i]
            index+=1
    del list[index:]
delete_an_even_number(list01)
print(list01)
