import os
def cope(file3,file4):
    with open(file3,"r") as file:
        with open(file4,"w") as filee:
            filee.write(file.read())
a = r'/Users/apple/Desktop/test2/A.txt'
b = r'/Users/apple/Desktop/test2/D.txt'
cope(a,b)