"""
    调用下列函数
"""
# 不定长参数
# 位置实参数量无限    关键字实参数量无限
def func01(*args, **kwargs):  # 多 合 一
    print(args)
    print(kwargs)


func01() #()
	 #{}
func01(1, 2, 3, 4, 5, a=1, b=2, c=3) #(1, 2, 3, 4, 5)
				     #{'a': 1, 'b': 2, 'c': 3}

list01 = [1, 2, 3] 
dict01 = {"a": 1, "b": 2}
func01(*list01, **dict01)  # 一 拆 多  #(1, 2, 3)
			               #{'a': 1, 'b': 2}


# 位置形参 星号元组形参 命名关键字形参 双星号字典形参
def func02(p1, p2, *args, p3, p4=4, **kwargs):
    print(p1) 
    print(p2) 
    print(args)
    print(p3)
    print(p4)
    print(kwargs)

# 位置实参,关键字实参
func02(1, 2, 3, 4, 5, p3=6, p4=7, p5=8, p6=9)	# 1
						# 2
						# (3, 4, 5)
						# 6
						# 7
						# {'p5': 8, 'p6': 9}
															
func02(1, 2, p3=6)				#1
						#2
						#()
						#6
						#4
						#{}

func02(1, p2=2, p4=3, p5=4, p6=5, p3=6, )	#1
						#2
						#()
						#6
						#3
						#{'p5': 4, 'p6': 5}











