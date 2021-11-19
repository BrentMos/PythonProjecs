from tkinter import *
from tkinter import messagebox


def select():
    Selection = listbox1.curselection()
    if Selection:
        listbox2.insert(END, listbox1.get(ANCHOR))
        for i in reversed(Selection):
            listbox1.delete(i)
    else:
        messagebox.showwarning("Error", "U didn't select an item")


def select2():
    Selection = listbox2.curselection()
    if Selection:
        listbox1.insert(END, listbox2.get(ANCHOR))
        for i in reversed(Selection):
            listbox2.delete(i)
    else:
        messagebox.showwarning("Error", "U didn't select an item")


top = Tk()

Lijst = ['Multimedia', 'Windows 10', 'Word gevorderden', 'Word beginners', 'Python voor beginners']
top.geometry("750x650")
top.title("Listboxen")

listbox1 = Listbox(top, selectmode=SINGLE, height=10, width=20, bg="grey", activestyle='dotbox', font="Helvetica",
                   fg="yellow")

listbox2 = Listbox(top, height=10,
                   width=20,
                   bg="grey",
                   activestyle='dotbox',
                   font="Helvetica",
                   fg="yellow")

listbox1.insert(END, *Lijst)

Links = Button(top, text='-->', command=select)
Rechts = Button(top, text='<--', command=select2)

listbox1.place(x=100, y=150)
listbox2.place(x=450, y=150)
Links.place(x=350, y=175)
Rechts.place(x=350, y=250)
top.mainloop()
