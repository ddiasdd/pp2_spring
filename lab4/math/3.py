import math
def area(number,lenght):
    area_polygon = (number*lenght**2)/(4*math.tan(math.pi/number))
    return area_polygon
n = int(input())
l = int(input())
print(area(n,l))