import re
string = input()
str = string.split('_')
x = str[0] + ''.join(i.title() for i in str[1:])
print(x)