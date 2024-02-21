def square(N):
    for i in range(1,N+1):
        yield i**2
N = int(input())
square_num = square(N)
print(','.join(map(str,square_num)))