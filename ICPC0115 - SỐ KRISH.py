def gt(n):
    tich = 1
    for i in range(1, n+1):
        tich*= i
    return tich
def solve(n):
    n = str(n)
    tong = sum(gt(int(i)) for i in n)
    if tong == int(n):
        return True
    return False
for _ in range(int(input())):
    n = int(input())
    if solve(n):
        print("Yes")
    else:
        print("No")