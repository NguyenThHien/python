for _ in range(int(input())):
    n , k = map(int, input().split())
    a = list(map(int, input().split()))
    res = a[k:]+a[:k]
    print(" ".join(map(str, res)))
