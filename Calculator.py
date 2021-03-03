from tkinter import *
root=Tk()
root.geometry("655x433")
root.title("Calculator")
def bt_clear():
    global i
    i=""
    input_text.set("")


def bt_click(item):
    global i
    i=i+str(item)
    input_text.set(i)

def bt_equal():
    global i
    result=str(eval(i))
    input_text.set(result)
    i=""

i=""

input_text=StringVar()

frame1=Frame(root,bg="grey",borderwidth=12,relief=SUNKEN)
frame1.pack(side=TOP)

input_field=Entry(frame1,font="lucida 16 bold",textvariable=input_text)
input_field.pack(ipady=10)

bframe=Frame(root,bg="gray",relief=SUNKEN)
bframe.pack()

clear=Button(bframe,text="C",fg="black",command=lambda :bt_clear(),width=22,height=3).grid(row=0,column=0,columnspan=2)
divide=Button(bframe,text="/",fg="black",command=lambda :bt_click("/"),width=11,height=3).grid(row=0,column=2)

seven=Button(bframe,text="7",fg="black",command=lambda :bt_click(7),width=11,height=3).grid(row=1,column=0)
eight=Button(bframe,text="8",fg="black",command=lambda :bt_click(8),width=11,height=3).grid(row=1,column=1)
nine=Button(bframe,text="9",fg="black",command=lambda :bt_click(9),width=11,height=3).grid(row=1,column=2)

four=Button(bframe,text="4",fg="black",command=lambda :bt_click(4),width=11,height=3).grid(row=2,column=0)
five=Button(bframe,text="5",fg="black",command=lambda :bt_click(5),width=11,height=3).grid(row=2,column=1)
six=Button(bframe,text="6",fg="black",command=lambda :bt_click(6),width=11,height=3).grid(row=2,column=2)

one=Button(bframe,text="1",fg="black",command=lambda :bt_click(1),width=11,height=3).grid(row=3,column=0)
two=Button(bframe,text="2",fg="black",command=lambda :bt_click(2),width=11,height=3).grid(row=3,column=1)
three=Button(bframe,text="3",fg="black",command=lambda :bt_click(3),width=11,height=3).grid(row=3,column=2)

multiply=Button(bframe,text="*",fg="black",command=lambda :bt_click("*"),width=11,height=3).grid(row=4,column=0)
minus=Button(bframe,text="-",fg="black",command=lambda :bt_click("-"),width=11,height=3).grid(row=4,column=1)
plus=Button(bframe,text="+",fg="black",command=lambda :bt_click("+"),width=11,height=3).grid(row=4,column=2)

zero=Button(bframe,text="0",fg="black",command=lambda :bt_click(0),width=11,height=3).grid(row=5,column=0)
point=Button(bframe,text=".",fg="black",command=lambda :bt_click("."),width=11,height=3).grid(row=5,column=1)
equal=Button(bframe,text="=",fg="black",command=lambda :bt_equal(),width=11,height=3).grid(row=5,column=2)





root.mainloop()