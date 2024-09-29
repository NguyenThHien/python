import math
class complexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        return complexNumber(self.real+other.real, self.imaginary+other.imaginary)
    def __mul__(self, other):
        return complexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)
    def out(self):
        if self.imaginary > 0:
            return f"{self.real} + {self.imaginary}i"
        elif self.imaginary < 0:
             return f"{self.real} - {int(math.fabs(self.imaginary))}i"
        else:
            return f"{self.real}"
             
t = int(input())
for _ in range(t):
    res = []
    a, b, c, d = map(int, input().split())
    A = complexNumber(a, b)
    B = complexNumber(c, d)
    C = (A+B)*A
    D = (A+B)*(A+B)
    res.append(C.out())
    res.append(D.out())
    print(", ".join(res))
