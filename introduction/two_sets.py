n = int(input())
s = (n*(n+1))//2
if s%2:
    print('YES')
    k = n//2
    print(k+1)
    for i in range(1,n+1,2):
        print(i, end=' ')
    print()
    print(k)
    for i in range(2,n+1,2):
        print(i, end=' ')
    print()
else:
    print('NO')