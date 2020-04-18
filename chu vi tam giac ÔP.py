class tamgiac:
    def __init__(self,a,b,c):
        self.canh1=a
        self.canh2=b
        self.canh3=c
    def tinh(self):
        if self.canh1 + self.canh2 >self.canh3 and self.canh1 + self.canh3 >self.canh2 and self.canh3 + self.canh2 >self.canh1:
            self.chuvi= int(self.canh1) +int(self.canh2) + int(self.canh3)
            print(self.chuvi)
        else: print('đây không phải tam giác')

chuvi=tamgiac(3,4,5)
chuvi.tinh()

