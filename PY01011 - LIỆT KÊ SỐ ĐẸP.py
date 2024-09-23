def check(n):
    n = str(n)
    if len(n) % 2 == 1 or n != n[::-1]:
        return False
    for i in n:
        x = int(i)
        if x % 2 == 1:
            return False
    return True


T = int(input())
for _ in range(T):

    n = int(input())
    res = []
    for i in range(22, n):
        if check(i):
            res.append(i)
    print(" ".join(map(str, res)))

