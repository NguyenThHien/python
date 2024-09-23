for _ in range(int(input())):
    n, b = map(int, input().split())
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    while n > 0:
        remainder = n%b
        res.append(digits[remainder])
        n //= b
    print("".join(reversed(res)))
