from tkinter import *

root = Tk()
root.title('Calculator')
# root.iconbitmap('icons/Dtafalonso-Android-Lollipop-Calculator.ico')

e = Entry(root, width=26, borderwidth=3)
e.grid(row=0, column=0, columnspan=4, pady=10)

def buttonClear():
    e.delete(0, END)

def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def buttonAdd():
    first_number=e.get()
    global fnum
    global operation
    operation='Add'
    fnum=int(first_number)
    e.delete(0, END)

def buttonMulti():
    first_number=e.get()
    global fnum
    global operation
    fnum=int(first_number)
    operation='Multi'
    e.delete(0, END)

def buttonSub():
    first_number=e.get()
    global fnum
    global operation
    fnum=int(first_number)
    operation='Sub'
    e.delete(0, END)

def buttonDiv():
    first_number=e.get()
    global fnum
    global operation
    fnum=int(first_number)
    operation='Div'
    e.delete(0, END)

def buttonEqual():
    second_number=e.get()
    e.delete(0, END)

    if(operation=='Add'):
        e.insert(0, fnum + int(second_number))

    elif(operation=='Sub'):
        e.insert(0, fnum - int(second_number))

    elif(operation=='Multi'):
        e.insert(0, fnum * int(second_number))

    elif(operation=='Div'):
        e.insert(0, fnum / int(second_number))

button_1 = Button(root, text='1', height=3, width=6, command=lambda: buttonClick(1)).grid(row=1, column=0)
button_2 = Button(root, text='2', height=3, width=6, command=lambda: buttonClick(2)).grid(row=1, column=1)
button_3 = Button(root, text='3', height=3, width=6, command=lambda: buttonClick(3)).grid(row=1, column=2)
button_4 = Button(root, text='4', height=3, width=6, command=lambda: buttonClick(4)).grid(row=2, column=0)
button_5 = Button(root, text='5', height=3, width=6, command=lambda: buttonClick(5)).grid(row=2, column=1)
button_6 = Button(root, text='6', height=3, width=6, command=lambda: buttonClick(6)).grid(row=2, column=2)
button_7 = Button(root, text='7', height=3, width=6, command=lambda: buttonClick(7)).grid(row=3, column=0)
button_8 = Button(root, text='8', height=3, width=6, command=lambda: buttonClick(8)).grid(row=3, column=1)
button_9 = Button(root, text='9', height=3, width=6, command=lambda: buttonClick(9)).grid(row=3, column=2)
button_0 = Button(root, text='0', height=3, width=6, command=lambda: buttonClick(0)).grid(row=4, column=0)

button_a = Button(root, text='+', height=3, width=6, command=buttonAdd).grid(row=1, column=3)
button_s = Button(root, text='-', height=3, width=6, command=buttonSub).grid(row=2, column=3)
button_m = Button(root, text='x', height=3, width=6, command=buttonMulti).grid(row=3, column=3)
button_d = Button(root, text='÷', height=3, width=6, command=buttonDiv).grid(row=4, column=3)
button_e = Button(root, text='=', height=3, width=6, padx=27, command=buttonEqual).grid(row=4, column=1, columnspan=2)

button_clear = Button(root, text='clear', height=3, width=6, padx=27, command=buttonClear).grid(row=5, column=0, columnspan=2)
button_off = Button(root, text='OFF', height=3, width=6, padx=27, command=root.quit).grid(row=5, column=2, columnspan=2)


root.mainloop()