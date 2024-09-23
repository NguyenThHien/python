import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        y = math.gcd(self.tu, self.mau)
        self.tu = self.tu // y
        self.mau = self.mau // y
        print(f'{self.tu}/{self.mau}')
n, m = map(int, input().split())
p1 = PhanSo(n, m)
p1.rutgon()