import math
def cnt(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def check2(n):
    if not cnt(n):
        return False
    n = str(n)
    s = n[::-1]
    if (not cnt((int(s)))) or s == n:
        return False
    
    
    
    
    return True


for _ in range(int(input())):
    n = int(input())
    res = []
    for i in range(13, n):
        x = str(i)
        x = int(x[::-1])
        if check2(i)  and x not in res and x < n: 
            print(i, x, end = ' ' )
            res.append(i)
            res.append(x)
    print()
    

    