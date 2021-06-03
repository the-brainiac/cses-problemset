import math 
from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10**6)
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

"""
def print(*args):
	for i in args:
		sys.stdout.write(str(i))
		sys.stdout.write(' ')
	sys.stdout.write('\n')
"""

total_childs=[1]*(1000001)

def dfs(graph,cur):
    
    for nbr in graph[cur]:
        
        dfs(graph,nbr)
        total_childs[cur]+=total_childs[nbr]


if __name__ == '__main__':
    n = readInt()
    arr = intList()
    graph = defaultdict(list)

    for i in range(n-1):
        u, v = arr[i], i+2
        graph[u-1].append(v-1)

    dfs(graph, 0)
    for i in range(n):
    	print(total_childs[i]-1,end=' ')
