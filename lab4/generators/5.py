def returns(N):
    for i in range(N,0,-1):
        yield i
N = int(input())
result = returns(N)
print(','.join(map(str,result)))