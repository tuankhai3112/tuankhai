from tkinter import *
class giaiptbac2:
    def __init__(self):
        self.root=Tk()
        self.tittle=self.root.title('Phương trình bậc 2')
        self.geometry=self.root.geometry('400x400')
    def display(self):
        self.lb_1 = Label(self.root,text='Entry a,b,c',font=('Segoe UI', 12),padx=15,pady=20).place(x=0,y=0)
        self.entry_a = Entry(self.root,width=20)
        self.a = self.entry_a.get()
        self.entry_a.place(x=50,y=50)
        self.entry_b = Entry(self.root, width=20)
        self.b = self.entry_b.get()
        self.entry_b.place(x=150,y=150)
        self.entry_c = Entry(self.root, width=20)
        self.c = self.entry_c.get()
        self.entry_c.place(x=250,y=250)
    def func_solve(self):
        if int(self.a) == 0:
            lb_none = Label(self.root, text='Not is ptb2').place(x=500, y=500)
            exit()

        self.d = int(self.b) * int(self.b) - 4 * int(self.a) * int(self.c)

        if self.d < 0:
                lb_vonghiem = Label(self.root, text='Pt vo nghiem').place(x=500, y=500)

        if self.d == 0:
            self.x = (-int(self.b) + self.d ** (1 / 2)) / 2*int(self.a)
            lb_nghiemkep = Label(self.root, text='pt co nghiem kep' + str(x)).place(x=500, y=500)
        if self.d > 0:
            self.x1 = (-float(self.b) + self.d ** (1 / 2)) / (2*float(self.a))
            self.x2 = (-float(self.b) - self.d ** (1 / 2)) / (2*float(self.a))
            self.lb_x1 = Label(self.root, text='x1=' + str(x1)).place(x=500, y=500)
            self.lb_x2 = Label(self.root, text='x2=' + str(x2)).place(x=600, y=500)
        self.button_1 = Button(self.root, text='Solve', fg='white', bg='lime', font=('Segoe UI', 12), padx=10, pady=5,
                               command=func_solve).grid(column=3, row=5)

        self.root.mainloop()



giaipt=giaiptbac2()
giaipt.display()
giaipt.func_solve()