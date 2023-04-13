from tkinter import *


class MidtermProblem2:
    def __init__(self, name):

        self.title = Label(name, text="My Full Name", font="Verdana", foreground="Red")
        self.title.place(x=250, y=50)
        self.givenname = Label(name, text="Enter Given Name: ", foreground="Red")
        self.givenname.place(x=100, y=100)
        self.middlename = Label(name, text="Enter Middle Name: ", foreground="Red")
        self.middlename.place(x=100, y=150)
        self.lastname = Label(name, text="Enter Last Name: ", foreground="Red")
        self.lastname.place(x=100, y=200)
        self.fullname = Label(name, text="My Full Name is: ", foreground="Red")
        self.fullname.place(x=100, y=250)
        self.txt1 = Entry(name, bd=1)
        self.txt1.place(x=350, y=100)
        self.txt2 = Entry(name, bd=1)
        self.txt2.place(x=350, y=150)
        self.txt3 = Entry(name, bd=1)
        self.txt3.place(x=350, y=200)
        self.txt4 = Entry(name, width=40, bd=1, foreground="Red")
        self.txt4.place(x=350, y=250)
        self.btnsfn = Button(name, text="Show Full Name")
        self.btnsfn.place(x=250, y=350)
        self.btnsfn.bind('<Button-1>', self.sfn)
        self.btnclr = Button(name, text="Clear All")
        self.btnclr.place(x=250, y=400)
        self.btnclr.bind('<Button-1>', self.clr)

    def sfn(self, sfn):
        self.txt4.delete(0, 'end')
        givenname = str(self.txt1.get())
        middlename = str(self.txt2.get())
        lastname = str(self.txt3.get())
        fullname = lastname+', '+givenname+' '+middlename
        self.txt4.insert('end', str(fullname))

    def clr(self, clr):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')


window = Tk()
myWin = MidtermProblem2(window)
window.geometry("700x500")
window.title("Midterm Exam Problem 2")
window.mainloop()
