import re
str = input()
x = re.findall("[a][b]{2,3}",str)
print(x)