import math
def checknt(n):
    if n == 1:
        return False
    for i in range(2, round(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def tongchuso(n):
    return sum(int(i) for i in str(n))
def checkyc(a, b):
    n = math.gcd(a, b)
    k = tongchuso(n)
    if(checknt(k)):
        return True
    return False

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if(checkyc(a, b)):
        print("YES")
    else:
        print("NO")