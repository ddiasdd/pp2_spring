import re
str = input()
x = re.findall("[A-Z]{1}[a-z]+",str)
print(x)