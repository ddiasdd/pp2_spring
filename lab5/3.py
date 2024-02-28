import re
str = input()
x = re.findall("[a-z]+_[a-z]+",str)
print(x)