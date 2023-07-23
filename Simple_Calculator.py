from tkinter import * 
def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnclear():
    global val
    val=" "
    data.set(" ")

def btnequal():
    global val
    result=str(eval(val))
    data.set(result)

obj = Tk()
obj.title("Calculator")
# label=Label(obj,text="Amit's Calculator",bg="light blue")
# label.pack()
obj.geometry("300x300")
val=" "
data=StringVar()
display=Entry(obj,textvariable=data,bd=40,justify="right",bg="light Green",font=(15))
display.grid(row=0,columnspan=4)
btn7=Button(obj,text="7",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick(7))
btn7.grid(row=1,column=0)
btn8=Button(obj,text="8",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick(8))
btn8.grid(row=1,column=1)
btn9=Button(obj,text="9",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick(9))
btn9.grid(row=1,column=2)
btnadd=Button(obj,text="+",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick('+'))
btnadd.grid(row=1,column=3)
btn4=Button(obj,text="4",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick(4))
btn4.grid(row=2,column=0)
btn5=Button(obj,text="5",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick(5))
btn5.grid(row=2,column=1)
btn6=Button(obj,text="6",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick(6))
btn6.grid(row=2,column=2)
btnsub=Button(obj,text="-",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick('-'))
btnsub.grid(row=2,column=3)
btn1=Button(obj,text="1",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick(1))
btn1.grid(row=3,column=0)
btn2=Button(obj,text="2",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick(2))
btn2.grid(row=3,column=1)
btn3=Button(obj,text="3",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick(3))
btn3.grid(row=3,column=2)
btnmul=Button(obj,text="*",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick('*'))
btnmul.grid(row=3,column=3)
btn0=Button(obj,text="0",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick(0))
btn0.grid(row=4,column=0)
btnclr=Button(obj,text="C",font=("bold",13),bd=10,height=1,width=5,command=btnclear)
btnclr.grid(row=4,column=1)
btneq=Button(obj,text="=",font=("bold",13),bd=10,height=1,width=5,command=btnequal)
btneq.grid(row=4,column=2)
btndiv=Button(obj,text="÷",font=("bold",13),bd=10,height=1,width=5,command=lambda:btnclick('/'))
btndiv.grid(row=4,column=3)
obj.resizable(0,0)
obj.mainloop()