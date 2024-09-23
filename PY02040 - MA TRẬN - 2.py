n = int(input())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
k = int(input())
tong1 = 0
tong2 = 0
for i in range(n):
    for j in range(n):
        if j < n - 1 - i:
            tong1 += a[i][j]
        elif j >  n - 1 - i:
            tong2 += a[i][j]

x = tong2 - tong1
x = abs(x)
if x <= k:
    print("YES")
    print(x)
else:
    print("NO")
    print(x)