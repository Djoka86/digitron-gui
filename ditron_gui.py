# from _ast import Lambda
from tkinter import *

root = Tk()
root.title('prosti digitron')
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    postojece = e.get()
    e.delete(0, END)
    e.insert(0, str(postojece) + str(number))



def button_clear():
    e.delete(0, END)


def button_equal():
    drugi_broj = e.get()
    d_broj = int(drugi_broj)
    e.delete(0, END)
    if math == 'sabiranje':
        e.insert(0, p_broj + d_broj)
    if math == 'oduzimanje':
        e.insert(0, p_broj - d_broj)
    if math == 'mnozenje':
        e.insert(0, p_broj * d_broj)
    if math == 'deljenje':
        e.insert(0, p_broj / d_broj)


def button_add():
    prvi_broj = e.get()
    global p_broj
    global math
    math = 'sabiranje'
    p_broj = int(prvi_broj)
    e.delete(0, END)


def button_subtraction():
    prvi_broj = e.get()
    global p_broj
    global math
    math = 'oduzimanje'
    p_broj = int(prvi_broj)
    e.delete(0, END)


def button_multiplication():
    prvi_broj = e.get()
    global p_broj
    global math
    math = 'mnozenje'
    p_broj = int(prvi_broj)
    e.delete(0, END)


def button_division():
    prvi_broj = e.get()
    global p_broj
    global math
    math = 'deljenje'
    p_broj = int(prvi_broj)
    e.delete(0, END)


#  definisemo dugmice//// treba ubaciti Lambda u   command=button_click)
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_clear = Button(root, text='ce', padx=79, pady=20, command=button_clear)
button_equal = Button(root, text='=', padx=39, pady=20, command=button_equal)
button_subtraction = Button(root, text='-', padx=39, pady=20, command=button_subtraction)
button_multiplication = Button(root, text='*', padx=39, pady=20, command=button_multiplication)
button_division = Button(root, text='/', padx=39, pady=20, command=button_division)
button_add = Button(root, text='+', padx=39, pady=20, command=button_add)

#  postavljamo na ekran
button9.grid(row=1, column=2)
button8.grid(row=1, column=1)
button7.grid(row=1, column=0)
button6.grid(row=2, column=2)
button5.grid(row=2, column=1)
button4.grid(row=2, column=0)
button3.grid(row=3, column=2)
button2.grid(row=3, column=1)
button1.grid(row=3, column=0)
button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=6, column=1, columnspan=2)
button_subtraction.grid(row=5, column=1)
button_multiplication.grid(row=5, column=2)
button_division.grid(row=6, column=0)

root = mainloop()
