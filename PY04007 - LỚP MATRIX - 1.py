class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a
    def multiply_with_transpose(self):
        res = [[0]*self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.m):
                    res[i][j]+=self.a[i][k]*self.a[j][k]
        return res
t = int(input())
for _ in range(t):
    n , m = map(int, input().split())
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    matrix = Matrix(n, m, a)
    for i in matrix.multiply_with_transpose():
        print(" ".join(map(str, i)))

