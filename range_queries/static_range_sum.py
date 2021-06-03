n, q = map(int,input().split())
arr = list(map(int,input().split()))
res = [0]*(n+1)
for i in range(n):
    res[i+1] = res[i] + arr[i]
for i in range(q):
    a, b = map(int,input().split())
    print(res[b]-res[a-1])