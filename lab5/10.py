import re
str = input()
x = re.findall(r"[A-Z][a-z0-9]*",str)
y = '_'.join(i.lower() for i in x)
print(y)