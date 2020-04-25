import tkinter as tk
class phuongtrinh:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title('Giải phương trình')
        self.root.geometry('295x400')

    

    def ptb2(self):
        self.root1 = tk.Tk()
        self.root1.title('Ptb2')
        self.root1.geometry('350x250')
        self.lb_0 = tk.Label(self.root1, text='Phương trình :', font=('Segoe UI', 14))
        self.lb_0.place(x=10,y=10)
        self.lb_1=tk.Label(self.root1,text='Answer',font= ('Segoe UI',14))
        self.lb_1.place(x=20,y=120)

        self.but_solve1=tk.Button(self.root1,text='SOLVE',fg='white',bg='lightgrey',width=10,height=1,
                                command=lambda: self.giaiptbac2,font= ('Segoe UI',12))
        self.but_solve1.place(x=230,y=90)
        self.lb_x1 = tk.Label(self.root1,text='x² + ',font=('Segoe UI',14)).place(x=80,y=50)
        self.lb_x2 = tk.Label(self.root1, text='x + ', font=('Segoe UI', 14)).place(x=200, y=50)
        self.lb_x0 =tk.Label(self.root1, text=' = 0', font=('Segoe UI', 14)).place(x=300, y=50)
        self.e_x1 = tk.Entry(self.root1, width=10).place(x=10, y=50, height=25)
        self.e_x2 = tk.Entry(self.root1, width=10).place(x=130, y=50, height=25)
        self.e_x3 = tk.Entry(self.root1, width=10).place(x=240, y=50, height=25)
        self.ans = tk.Text(self.root1, height=4, width=30,font=('Segoe UI', 14))
        self.ans.place(x=10, y=150, height=80)

    def giaiptbac2(self):

        self.a = eval(self.e_x1.get())
        self.b = eval(self.e_x2.get())
        self.c = eval(self.e_x3.get())

        self.d = self.b ** 2 - 4 * self.a * self.c
        if self.a == 0:
            self.x0=-self.c/self.b
            self.ans.tk.insert(0,'x = '+ str(self.x0))
        else:
            if self.d < 0:
                self.ans.tk.insert(0,'Phương trình vô nghiệm')
            if self.d == 0:
                self.x = (-self.b + self.d ** (1 / 2) / (2 * self.a))
                self.ans.tk.insert(0,'x = '+ str(self.x))
            if self.d > 0:
                self.x1 = (-self.b + self.d ** (1 / 2) / (2 * self.a))
                self.x2 = (-self.b + self.d ** (1 / 2) / (2 * self.a))
                self.ans.tk.insert(0, 'x = ' + str(self.x0)+'\n')
                self.ans.tk.insert(0, 'x = ' + str(self.x0))
        
    def display(self):
        self.lb_ques=tk.Label(self.root,text='PyNoneCal',font=('Segoe UI',14),fg='white',bg='springgreen',padx=100,pady=20)
        self.lb_ques.place(x=0,y=0)
        self.btn_1=tk.Button(self.root,text='Phương trình bậc 2',command=self.ptb2,padx=40,pady=10).place(x=50,y=80)


    def start(self):
        self.root.mainloop()
        self.root1.mainloop()

if __name__=='__main__':
    giaipt=phuongtrinh()
    giaipt.display()
    giaipt.start()
