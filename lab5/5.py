import re
str = input()
x = re.findall("a.*b",str)
print(x)