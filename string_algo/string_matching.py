s = input().strip()
k = input().strip()
res = 0
for i in range(len(s)-len(k)+1):
    if s[i:i+len(k)] == k:
        res += 1
print(res)