import math
def cnt_coprimes(n):
    cnt = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            cnt += 1
    return cnt
def nt(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, round(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
T = int(input())
for _ in range(T):
    n = int(input())
    k = cnt_coprimes(n)
    if(nt(k)):
        print("YES")
    else:
        print("NO")