from tkinter import*

class MyWindow:
    def __init__(self,win):
        win.configure(bg='#798645')
        #commom widgets
        self.Label1 = Label (win,fg="#798645",text="*＊✿❀Calculator❀✿＊*", font=("Century Gothic", 20))
        self.Label1.place(x=100, y=40)
        self.Label2 = Label (win,fg="#798645",text="Number 1:")
        self.Label2.place(x=70, y=100)
        self.Label3 = Label(win, fg="#798645", text="Number 2:")
        self.Label3.place(x=70, y=150)
        self.Label4 = Label(win, fg="#798645", text="Result:")
        self.Label4.place(x=70, y=200)

        self.Entry1= Entry(win, bd=5)
        self.Entry1.place(x=170, y=98)
        self.Entry2 = Entry(win, bd=5)
        self.Entry2.place(x=170, y=148)
        self.Entry3 = Entry(win, bd=5)
        self.Entry3.place(x=170, y=198)

        self.Button1=Button(win, fg="#798645", text="Add",command=self.add)
        self.Button1.place(x=90, y=300)
        self.Button2=Button(win, fg="#798645", text="Subtract",command=self.subtract)
        self.Button2.place(x=170, y=300)
        self.Button3=Button(win, fg="#798645", text="Multiply",command=self.multiply)
        self.Button3.place(x=265, y=300)
        self.Button4=Button(win, fg="#798645", text="Divide",command=self.divide)
        self.Button4.place(x=360, y=300)

    def add(self):
        self.Entry3.delete(0,'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def subtract(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def multiply(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def divide(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))




window=Tk()
MyWin=MyWindow(window)

window.geometry("500x400+10+10")
window.title("Standard Calculator")
window.mainloop()