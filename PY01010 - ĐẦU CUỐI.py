T = int(input())
for _ in range(T):
    n = str(input())
    first_two = n[:2]
    last_two = n[-2:]
    if first_two == last_two :
        print("YES")
    else:
        print("NO")