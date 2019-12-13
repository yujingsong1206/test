import re
info = "姓名:tom1990  生日:2019年12月13日 大学:2039-12-13"

#正则表达式  贪婪模式    .*生日.*?\d{4}
#从头开始
# result = re.match(".*生日.*?(\d{4}).*大学.*?(\d{4})", info)
# print(result.group())
# print(result.group(1))
# print(result.group(2))

#从符合的某个字符开始
# result = re.search("生日.*?(\d{4})", info)
# print(result.group())
# print(result.group(1))

# result = re.sub("\d{4}" ,"2020", info)
# print(result)
# print(info)

name = "my name is Tom"
result = re.search("tom", name, re.IGNORECASE)
print(result.group())
