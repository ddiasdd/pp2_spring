def area(height,first,second):
    area_trapezoidal = (first+second)*(height/2)
    return area_trapezoidal
area_tr = area(5,5,6)
print(area_tr)