
if __name__ == '__main__':
# for _ in range(readInt()):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # print('YES' if solve() else 'NO')
    dp = [10**9]*(x+1)
    dp[0] = 0
    for p in range(1,x+1):
        for i in arr:
            if p-i >= 0:
                dp[p] = min(dp[p], dp[p-i]+1)
    res = dp[x]
    if res == 10**9:
        print(-1)
    else:
        print(res)