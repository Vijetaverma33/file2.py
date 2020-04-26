from tkinter import *

me=Tk()
me.title("Calculator")
melabel=Label(me,text="CALCULATOR",font="broadway 20 italic",bg= 'white',fg='blue')
melabel.grid(row=1,column=0,columnspan=5)
me.config(background='light gray')

textin=StringVar()
operator=''

def clickbutton(number):
    global operator
    operator=operator+str(number)
    textin.set(operator)
def equalbutton():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator = ''
def equalbutton():
    global operator
    sub=str(eval(operator))
    textin.set(sub)
    operator = ''
def equalbutton():
    global operator
    mul=str(eval(operator))
    textin.set(mul)
    operator = ''
def equalbutton():
    global operator
    div=str(eval(operator))
    textin.set(div)
    operator = ''
def clearbutton():
    textin.set('')

metext=Entry(me,font=("arial",16,"bold"),textvar=textin,bd=5,bg='powder blue')
metext.grid(row=2,column=0,columnspan=5)
button1=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="1",height=2,width=4,command=lambda:clickbutton(1))
button1.grid(row=3,column=0)
button2=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="2",height=2,width=4,command=lambda:clickbutton(2))
button2.grid(row=4,column=0)
button3=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="3",height=2,width=4,command=lambda:clickbutton(3))
button3.grid(row=5,column=0)
button4=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="4",height=2,width=4,command=lambda:clickbutton(4))
button4.grid(row=3,column=1)
button5=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="5",height=2,width=4,command=lambda:clickbutton(5))
button5.grid(row=4,column=1)
button6=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="6",height=2,width=4,command=lambda:clickbutton(6))
button6.grid(row=5,column=1)
button7=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="7",height=2,width=4,command=lambda:clickbutton(7))
button7.grid(row=3,column=2)
button8=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="8",height=2,width=4,command=lambda:clickbutton(8))
button8.grid(row=4,column=2)
button9=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="9",height=2,width=4,command=lambda:clickbutton(9))
button9.grid(row=5,column=2)
button10=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="+",height=2,width=4,command=lambda:clickbutton("+"))
button10.grid(row=3,column=3)
button11=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="-",height=2,width=4,command=lambda:clickbutton("-"))
button11.grid(row=4,column=3)
button12=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="*",height=2,width=4,command=lambda:clickbutton("*"))
button12.grid(row=5,column=3)
#zero
button14=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="0",height=2,width=4,command=lambda:clickbutton(0))
button14.grid(row=6,column=0)
#dot
button15=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text=".",height=2,width=9,command=lambda:clickbutton('.'))
button15.grid(row=6,column=1,columnspan=2)
#/
button16=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="/",height=2,width=4,command=lambda:clickbutton('/'))
button16.grid(row=6,column=3)
# clear
button13 = Button(me, font=("arial", 12, "bold"), bg='white', bd=2, text="CE", height=10, width=4, command=clearbutton)
button13.grid(row=3, column=4, rowspan=4)
#=
button17=Button(me,font=("arial",12,"bold"),bg='white',bd=2,text="=",height=2,width=24,command=equalbutton)
button17.grid(row=7,column=0,columnspan=5)

me.mainloop()
