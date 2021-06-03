import math 
from collections import Counter, defaultdict
import sys
# sys.setrecursionlimit(10**6)

"""
# Template Designed By: the_brainiac (Shivshanker Singh)
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


def print(*args):
	for i in args:
		sys.stdout.write(str(i))
		sys.stdout.write(' ')
	sys.stdout.write('\n')

def prefix_sum(arr):
    res = [[0 for j in range(n+1)] for i in range(n+1)]
    # res = defaultdict(Counter)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '*':
                res[i+1][j+1] = res[i+1][j] + 1
            else:
                res[i+1][j+1] = res[i+1][j]
               
    for j in range(n):
        for i in range(n):
            res[i+1][j+1] += res[i][j+1]
    return res


if __name__ == '__main__':
# for _ in range(readInt()):
    # n = readInt()
    n, q = intMap()
    arr = []
    for i in range(n):
        arr.append(input().strip())
    res = prefix_sum(arr)
    
    for i in range(q):
        x1, y1, x2, y2 = intMap()
        print(res[x2][y2] - res[x2][y1-1] - res[x1-1][y2] + res[x1-1][y1-1])