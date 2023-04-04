from tkinter import *
class TempConversion:
    def __init__(self, temp):

        self.lbl1 = Label(temp, text="Temperature")
        self.lbl1.place(x=100, y=50)
        self.lbl2 = Label(temp, text="F° to C°")
        self.lbl2.place(x=100, y=100)
        self.lbl3 = Label(temp, text="K to C°")
        self.lbl3.place(x=100, y=150)
        self.lbl4 = Label(temp, text="C° to F°")
        self.lbl4.place(x=100, y=200)
        self.lbl5 = Label(temp, text="K to F°")
        self.lbl5.place(x=100, y=250)
        self.lbl6 = Label(temp, text="C° to K")
        self.lbl6.place(x=100, y=300)
        self.lbl7 = Label(temp, text="F° to K")
        self.lbl7.place(x=100, y=350)
        self.txt1 = Entry(temp, bd=1)
        self.txt1.place(x=200, y=50)
        self.txt2 = Entry(temp, bd=2)
        self.txt2.place(x=200, y=100)
        self.txt3 = Entry(temp, bd=3)
        self.txt3.place(x=200, y=150)
        self.txt4 = Entry(temp, bd=4)
        self.txt4.place(x=200, y=200)
        self.txt5 = Entry(temp, bd=5)
        self.txt5.place(x=200, y=250)
        self.txt6 = Entry(temp, bd=6)
        self.txt6.place(x=200, y=300)
        self.txt7 = Entry(temp, bd=7)
        self.txt7.place(x=200, y=350)

        self.btnfc = Button(temp, text="F° to C°")
        self.btnfc.place(x=100, y=400)
        self.btnfc.bind('<Button-1>', self.fc)

        self.btnkc = Button(temp, text="K to C°", command=self.kc)
        self.btnkc.place(x=200, y=400)

        self.btncf = Button(temp, text="C° to F°")
        self.btncf.place(x=100, y=450)
        self.btncf.bind('<Button-1>', self.cf)

        self.btnkf = Button(temp, text="K to F°", command=self.kf)
        self.btnkf.place(x=200, y=450)

        self.btnck = Button(temp, text="C° to K")
        self.btnck.place(x=100, y=500)
        self.btnck.bind('<Button-1>', self.ck)

        self.btnfk = Button(temp, text="F° to K", command=self.fk)
        self.btnfk.place(x=200, y=500)

    def fc(self,fc):
        self.txt2.delete(0, 'end')
        num1 = float(self.txt1.get())
        result = (num1 - 32) * 5/9
        self.txt2.insert(END, str(result))

    def kc(self):
        self.txt3.delete(0, 'end')
        num1 = float(self.txt1.get())
        result = num1 - 273.15
        self.txt3.insert(END, str(result))

    def cf(self,cf):
        self.txt4.delete(0, 'end')
        num1 = float(self.txt1.get())
        result = (num1 * 9/5) + 32
        self.txt4.insert(END, str(result))

    def kf(self):
        self.txt5.delete(0, 'end')
        num1 = float(self.txt1.get())
        result = (num1 - 273.15) * 9/5 + 32
        self.txt5.insert(END, str(result))

    def ck(self,ck):
        self.txt6.delete(0, 'end')
        num1 = float(self.txt1.get())
        result = num1 + 273.15
        self.txt6.insert(END, str(result))

    def fk(self):
        self.txt7.delete(0, 'end')
        num1 = float(self.txt1.get())
        result = (num1 - 32) * 5/9 + 273.15
        self.txt7.insert(END, str(result))

window = Tk()
mywin = TempConversion(window)
window.geometry("1000x600+10+10")
window.title("Temperature Conversion")
window.mainloop()