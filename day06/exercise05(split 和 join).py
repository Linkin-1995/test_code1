# 将下列英文语句按照单词进行翻转.
# To have a government that is of people by people for people
# people for people by people of is that government a have To

# 提示：按照空格拆分英文语句,翻转列表,用空格连接为字符串
sentence = "To have a government that is of people by people for people"
list_words = sentence.split(" ")
str_result = " ".join(list_words[::-1])
print(str_result)
