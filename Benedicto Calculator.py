from tkinter import *
class MyWindow:
    def __init__(self,win):

#widgets start from here
        self.lbl1 = Label(win,text="1st No.")     #for label widget
        self.lbl1.place(x=100,y=50)
        self.lbl2 = Label(win, text= "2nd No.")
        self.lbl2.place(x=100,y=100)
        self.lbl3 = Label(win, text="Result")
        self.lbl3.place(x=100,y=150)
        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=200,y=50)
        self.txt2 = Entry(win,bd=1)
        self.txt2.place(x=200,y=100)
        self.txt3 = Entry(win,bd=3)
        self.txt3.place(x=200,y=150)

        self.btnadd = Button(win,text="Add")
        self.btnadd.place(x=100, y=200)
        self.btnadd.bind('<Button-1>',self.add)

        self.btnsub = Button(win,text="Subtract", command = self.sub)
        self.btnsub.place(x=200, y=200)

        self.btnmultiply = Button(win,text="Multiply")
        self.btnmultiply.place(x=100,y=250)
        self.btnmultiply.bind('<Button-1>', self.multiply)

        self.btndivide = Button(win,text="Divide", command = self.divide)
        self.btndivide.place(x=200,y=250)


    def add(self,add):
        self.txt3.delete(0,'end')
        num1 = float(self.txt1.get())
        num2 = float(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END, str(result))

    def sub(self):
        self.txt3.delete(0,'end')
        num1 = float(self.txt1.get())
        num2 = float(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

    def multiply(self,multiply):
        self.txt3.delete(0,'end')
        num1 = float(self.txt1.get())
        num2 = float(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))

    def divide(self):
        self.txt3.delete(0, 'end')
        num1 = float(self.txt1.get())
        num2 = float(self.txt2.get())
        result = num1 / num2
        self.txt3.insert(END, str(result))


window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()







