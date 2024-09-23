def cnt_y(n, x, m):
    year = 0
    current_amount = n
    while current_amount < m :
        current_amount *= (1+x/100)
        year += 1
    return year
T = int(input())
for _ in range(T):
    n, x, m = map(float, input().split())
    res = cnt_y(n, x, m)
    print(res)