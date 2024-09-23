def check(n):
    k = n[-2::]
    if k == "86":
        return True
    else:
        return False
T = int(input())
for _ in range(T):
    n = str(input())
    if(check(n)):
        print("YES")
    else:
        print("NO")