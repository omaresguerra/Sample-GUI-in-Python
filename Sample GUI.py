from tkinter import *
root = Tk()

def compute():
    num1 = eval(ent1.get())
    num2 = eval(ent2.get())
    total = num1 + num2
    ent3.insert(0,total)

def delete():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)


item1 = Label(text='Item1:')
item2 = Label(text='Item2:')
item3 = Label(text='Total:')
item1.grid(row=0, column=0)
item2.grid(row=1, column=0)
item3.grid(row=2, column=0)

ent1 = Entry()
ent2 = Entry()
ent3 = Entry()
ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)
ent3.grid(row=2, column=1)

btnCompute = Button(text = 'Compute', command=compute)
btnDelete = Button(text = 'Delete', command=delete)

btnCompute.grid(row=3, column=1)
btnDelete.grid(row=5, column=1)


mainloop()
