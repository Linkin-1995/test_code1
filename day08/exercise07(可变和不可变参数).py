def func01(p1, p2, p3):
    p1 = ["b"]
    p2["a"] = "B" # 修改可变
    p3[0] = ["b"]# 修改可变


data01 = "a" # 不可变
data02 = {"a": "A"} # 可变
data03 = ["a"] # 可变
func01(data01, data02, data03)
print(data01)  # "a"
print(data02)  # {"a": "B"}
print(data03)  # [["b"]]
