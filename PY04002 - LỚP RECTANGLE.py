class Rectangle:
    def __init__(self, chieudai, chieurong, mau):
        self.chieudai = chieudai
        self.chieurong = chieurong
        self.mau = mau
    def check(self):
        x = self.chieudai
        y = self.chieurong
        if x <=0 or y<=0:
            return False
        return True
    def output(self) :
        if self.check() == 1 : print((self.chieudai + self.chieurong) * 2, self.chieurong * self.chieudai, self.mau.title(), sep = ' ')
        else : print('INVALID')



arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
r.output()