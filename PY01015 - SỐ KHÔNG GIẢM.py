def check(n):
    for i in range(1, len(n)):
        if n[i-1] > n[i]:
            return False
    return True
T = int(input())
for _ in range(T):
    n = str(input())
    if(check(n)):
        print("YES")
    else:
        print("NO")