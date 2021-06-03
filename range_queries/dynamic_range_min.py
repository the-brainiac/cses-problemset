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


def solve():
    pass
    
def generate_segment(arr):
    n = len(arr)
    n = 2**math.ceil(math.log2(n))
    seg = [0]*(2*n)
    for i in range(len(arr)):
        seg[n+i] = arr[i]
    for k in range(n-1, 0, -1):
        seg[k] = min(seg[2*k], seg[2*k+1])
    
    return seg

def update(idx, val):
    n = 2**math.ceil(math.log2(len(arr)))
    idx += n
    seg[idx] = val
    idx //= 2
    while idx > 0:
        seg[idx] = min(seg[2*idx], seg[2*idx + 1])
        idx //= 2


def query(a, b):
    n = 2**math.ceil(math.log2(len(arr)))
    a += n
    b += n
    res = 10**9
    while a <= b:
        if a%2:
            res = min(res, seg[a])
            a += 1
        if b%2 == 0:
            res = min(res, seg[b])
            b -= 1
        a //= 2
        b //= 2

    return res


if __name__ == '__main__':
# for _ in range(readInt()):
    # n = readInt()
    n, q = intMap()
    arr = intList()
    seg = generate_segment(arr)
    for q0 in range(q):
        ty, *args = intList()
        if ty == 1:
            idx, val = args
            update(idx-1, val)
        else:
            a, b = args
            print(query(a-1, b-1))
    
    