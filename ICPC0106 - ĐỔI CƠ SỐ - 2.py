for _ in range(int(input())):
    n = int(input())
    s = input()
    he_10 = 0
    length = len(s)
    for i in range(length):
        digit = int(s[length-1-i])
        he_10 += digit * (2 ** i)
   
    digits = "0123456789ABCDEF"
    res = []
    while he_10 > 0:
        remainder = he_10%n
        res.append(digits[remainder])
        he_10 //= n
    print("".join(reversed(res)))
