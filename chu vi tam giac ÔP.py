class tamgiac:
    def nhap(self):
        self.a=input('cạnh thứ nhất: ')
        self.b = input('Cạnh thứ hai:')
        self.c= input('Cạnh thứ ba:')
    def tinh(self):
        self.chuvi= int(self.a) +int(self.b) + int(self.c)
        return self.chuvi
chuvi=tamgiac()
chuvi.nhap()
print('Chu vi là',chuvi.tinh())
