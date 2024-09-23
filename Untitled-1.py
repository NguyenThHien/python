p = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    n, b = map(int, input().split() )
    res = []
    while(n>0):
        x = n%b
        res.append(p[x])
        n//b
    print("".join(map(str, res)))
