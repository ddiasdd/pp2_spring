import re
str = input()
x = re.findall("[A-Z][^A-Z]*",str)
y = ' '.join(x)
print(y)