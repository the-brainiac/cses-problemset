import math 
from collections import Counter, defaultdict
import sys
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


if __name__ == '__main__':
# for _ in range(readInt()):
    n = readInt()
    dp = [10**9]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for d in str(i):
            dp[i] = min(dp[i], dp[i-int(d)]+1)
    print(dp[n])