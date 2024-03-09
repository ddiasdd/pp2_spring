import os
def lines(file):
    with open(file,'r') as file:
        count = sum(1 for i in file)
        return count
file = r'/Users/apple/Desktop/test2/test.txt'
a = lines(file)
print(a)
import os
def lines(file):
    with open(file,'r') as file:
        count = 0
        for _ in file:
            count+=1
        return count
file = r'/Users/apple/Desktop/test2/test.txt'
a = lines(file)
print(a)



