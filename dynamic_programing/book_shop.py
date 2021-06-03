import math 
from collections import Counter, defaultdict
import sys
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
# sys.setrecursionlimit(10**6)

"""
# Template Designed By: Shivshanker Singh
# Note: If you find this template useful and want to use it then please don't just copy paste it 
        you can take ideas from this and make your own.
        because if you copy paste as it is then there are high chances that both of us will be plagiarized
        (because most of code will be same for small problems).
        So to avoid this please dont copy paste.
"""

mod       = 10**9 + 7
input     = sys.stdin.readline
readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
readStr   = lambda : input().strip()
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())
strList   = lambda : list(input().strip().split())


def print(*args, end='\n', sep=' '):
    for i in args:
        sys.stdout.write(str(i))
        sys.stdout.write(sep)
    sys.stdout.write(end)


def solve():
    pass
    
if __name__ == '__main__':
# for _ in range(readInt()):
    n, x = intMap()
    hrr = intList()
    srr = intList()
    
    dp = [[0]*(x+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, x+1):
            if j < hrr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-hrr[i-1]]+ srr[i-1])
    print(dp[n][x])