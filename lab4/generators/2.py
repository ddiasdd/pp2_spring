def even(N):
    for i in range(N+1):
        if(i%2==0):
            yield i
N = int(input())
result = even(N)
print(','.join(map(str,result)))