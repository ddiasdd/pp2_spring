import os
list = ['2','3']
with open('writing.txt','w') as file:
    for i in list:
        file.write(i+" ")
a = open('writing.txt')
print(a.read())