import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        self.rutgon()

    def rutgon(self):
        y = math.gcd(self.tu, self.mau)
        self.tu = self.tu // y
        self.mau = self.mau // y
        

    def cong(self, other):
        new_mau = self.mau * other.mau
        new_tu = self.tu * other.mau + other.tu * self.mau
        # Update the fraction to the result of the addition
        self.tu = new_tu
        self.mau = new_mau
        # Simplify the result
        self.rutgon()
        print(f'{self.tu}/{self.mau}')

a, b, c, d = map(int, input().split())
p1 = PhanSo(a, b)
p2 = PhanSo(c, d)
p1.cong(p2)


    


        