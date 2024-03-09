import time,math
def func(num,ms):
    time.sleep(ms/1000)
    return math.sqrt(num)
num = int(input())
ms = int(input())
print(func(num,ms))