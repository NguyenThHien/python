n = int(input())
a = []
for _ in range(n):
    a.append(input())
s = a[0]
res = 10**9
ok = 1
for i in range(len(s)):
    d = 0
    for j in range(n):
        x = a[j]
        for k in range(len(s)):
            if x == s:
                d+=k
                break
            x = x[1::]+x[0]
           
        if x!=s:
            ok = 0
    res = min(res, d)
    s = s[1::]+s[0]
# chọn 1 cái lm gốc để quay các cái còn lại tham chiếu
if ok == 0: print(-1)
else: print(res)