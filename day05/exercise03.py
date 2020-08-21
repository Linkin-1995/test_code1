"""
    content = "我是京师监狱狱长金海。"
    通过切片打印“京师监狱狱长”
    通过切片打印“长狱狱监师京”
    通过切片打印“我师狱海”
    倒序打印字符
"""
content = "我是京师监狱狱长金海。"
print(content[2: -3])
print(content[-4: 1:-1])
print(content[:: 3])
print(content[:: -1])
