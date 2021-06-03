n = int(input())
n_sum = n*(n+1)//2
given_sum = sum(list(map(int, input().split())))
print(n_sum-given_sum)