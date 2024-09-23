import math
def cnt(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def check2(n):
    if not cnt(int(n)):
        return False
    s = n[::-1]
    if not cnt((int(s))):
        return False
    tong = sum(int(i) for i in n)
    if not cnt(tong):
        return False
    for i in n:
        if  not cnt(int(i)):
            return False
    
    return True


for _ in range(int(input())):
    n = input()
   
    if check2(n):
        print("Yes")
    else:
        print("No")

    