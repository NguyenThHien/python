for _ in range(int(input())):
    n = str(input())
    if n[0] == n[-1::]:
        print("YES")
    else:
        print("NO")