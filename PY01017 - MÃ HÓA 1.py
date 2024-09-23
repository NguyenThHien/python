T = int(input())
for _ in range(T):
    n = str(input())
    res = []
    cnt = 1
    for i in range(1, len(n)):
        if n[i] == n[i-1]:
            cnt += 1
        else:
            res.append(f"{cnt}{n[i - 1]}")
            cnt = 1
    res.append(f"{cnt}{n[- 1]}")
    print("".join(res))


