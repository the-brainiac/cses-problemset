s = input()
l = 0
temp_len = 1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        temp_len += 1
    else:
        l = max(temp_len, l)
        temp_len = 1
l = max(temp_len, l)
print(l)