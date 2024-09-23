class ThiSinh:
    def __init__(self, ten, ns, d1, d2, d3):
        self.ten = ten
        self.ns = ns
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
      


    def tongdiem(self):
        tb  = self.d1+self.d2+self.d3
        return tb
    
    
s = input()
s1 = input()
s2 = float(input())
s3 = float(input())
s4 = float(input())
p1 = ThiSinh(s, s1, s2, s3, s4)
print(p1.ten, p1.ns, '{:.1f}'.format(p1.tongdiem()))


