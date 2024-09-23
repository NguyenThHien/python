T = int(input())
for _ in range(T):
    n = str(input())
    res = ""
    for i in range(0, len(n), 2):
        res += n[i]*int(n[i+1])
    print(res)
