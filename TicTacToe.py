from tkinter import *
root = Tk()
root.title('Tic-Tac-Toe')
root.iconbitmap('icons/cross.ico')

round=0
t=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def winDisp(sym):
    # Information Bar
    if sym!='D':
        if sym=='X':
            s='Player 2'
        elif sym=='O':
            s='Player 1'

        info = f'   {s} Won !   '
        label_header = Label(root, text=info, pady=7)
        label_header.grid(row=4, column=0, columnspan=3)
    else:
        info = f'   DRAW   '
        label_header = Label(root, text=info, pady=7)
        label_header.grid(row=4, column=0, columnspan=3)

def disableButtons(t):
    button_1 = Button(root, text=t[0], width=8, height=4, command=lambda: gameplay(0), state = DISABLED).grid(row=1, column=0)
    button_2 = Button(root, text=t[1], width=8, height=4, command=lambda: gameplay(1), state = DISABLED).grid(row=1, column=1)
    button_3 = Button(root, text=t[2], width=8, height=4, command=lambda: gameplay(2), state = DISABLED).grid(row=1, column=2)
    button_4 = Button(root, text=t[3], width=8, height=4, command=lambda: gameplay(3), state = DISABLED).grid(row=2, column=0)
    button_5 = Button(root, text=t[4], width=8, height=4, command=lambda: gameplay(4), state = DISABLED).grid(row=2, column=1)
    button_6 = Button(root, text=t[5], width=8, height=4, command=lambda: gameplay(5), state = DISABLED).grid(row=2, column=2)
    button_7 = Button(root, text=t[6], width=8, height=4, command=lambda: gameplay(6), state = DISABLED).grid(row=3, column=0)
    button_8 = Button(root, text=t[7], width=8, height=4, command=lambda: gameplay(7), state = DISABLED).grid(row=3, column=1)
    button_9 = Button(root, text=t[8], width=8, height=4, command=lambda: gameplay(8), state = DISABLED).grid(row=3, column=2)

def checkWin(t,sym):
    if t[0]==sym and t[1]==sym and t[2]==sym:
        print(f'{sym} won!')
        disableButtons(t)
        winDisp(sym)

    elif t[3]==sym and t[4]==sym and t[5]==sym:
        print(f'{sym} won!')
        disableButtons(t)
        winDisp(sym)

    elif t[6]==sym and t[7]==sym and t[8]==sym:
        print(f'{sym} won!')
        disableButtons(t)
        winDisp(sym)

    elif t[0]==sym and t[3]==sym and t[6]==sym:
        print(f'{sym} won!')
        disableButtons(t)
        winDisp(sym)

    elif t[1]==sym and t[7]==sym and t[4]==sym:
        print(f'{sym} won!')
        disableButtons(t)
        winDisp(sym)

    elif t[2]==sym and t[5]==sym and t[8]==sym:
        print(f'{sym} won!')
        disableButtons(t)
        winDisp(sym)

    elif t[0]==sym and t[4]==sym and t[8]==sym:
        print(f'{sym} won!')
        disableButtons(t)
        winDisp(sym)

    elif t[2]==sym and t[4]==sym and t[6]==sym:
        print(f'{sym} won!')
        disableButtons(t)
        winDisp(sym)

def gameplay(num):
    global round
    global t

    if round==0 or round%2==0 and round<9:
        t[num]='O'
        # Buttons
        button_1 = Button(root, text=t[0], width=8, height=4, command=lambda: gameplay(0)).grid(row=1, column=0)
        button_2 = Button(root, text=t[1], width=8, height=4, command=lambda: gameplay(1)).grid(row=1, column=1)
        button_3 = Button(root, text=t[2], width=8, height=4, command=lambda: gameplay(2)).grid(row=1, column=2)
        button_4 = Button(root, text=t[3], width=8, height=4, command=lambda: gameplay(3)).grid(row=2, column=0)
        button_5 = Button(root, text=t[4], width=8, height=4, command=lambda: gameplay(4)).grid(row=2, column=1)
        button_6 = Button(root, text=t[5], width=8, height=4, command=lambda: gameplay(5)).grid(row=2, column=2)
        button_7 = Button(root, text=t[6], width=8, height=4, command=lambda: gameplay(6)).grid(row=3, column=0)
        button_8 = Button(root, text=t[7], width=8, height=4, command=lambda: gameplay(7)).grid(row=3, column=1)
        button_9 = Button(root, text=t[8], width=8, height=4, command=lambda: gameplay(8)).grid(row=3, column=2)

        # Information Bar
        info = "   Player 2   "
        label_header = Label(root, text=info, pady=7)
        label_header.grid(row=4, column=0, columnspan=3)

    elif round!=0 or round%2!=0 and round<9:
        t[num]='X'
        # Buttons
        button_1 = Button(root, text=t[0], width=8, height=4, command=lambda: gameplay(0)).grid(row=1, column=0)
        button_2 = Button(root, text=t[1], width=8, height=4, command=lambda: gameplay(1)).grid(row=1, column=1)
        button_3 = Button(root, text=t[2], width=8, height=4, command=lambda: gameplay(2)).grid(row=1, column=2)
        button_4 = Button(root, text=t[3], width=8, height=4, command=lambda: gameplay(3)).grid(row=2, column=0)
        button_5 = Button(root, text=t[4], width=8, height=4, command=lambda: gameplay(4)).grid(row=2, column=1)
        button_6 = Button(root, text=t[5], width=8, height=4, command=lambda: gameplay(5)).grid(row=2, column=2)
        button_7 = Button(root, text=t[6], width=8, height=4, command=lambda: gameplay(6)).grid(row=3, column=0)
        button_8 = Button(root, text=t[7], width=8, height=4, command=lambda: gameplay(7)).grid(row=3, column=1)
        button_9 = Button(root, text=t[8], width=8, height=4, command=lambda: gameplay(8)).grid(row=3, column=2)

        # Information Bar
        info = "   Player 1   "
        label_header = Label(root, text=info, pady=7)
        label_header.grid(row=4, column=0, columnspan=3)

    round+=1
    # print(round)
    checkWin(t, 'X')
    checkWin(t, 'O')

    if round==9:
        print(t)
        winDisp('D')


#Status Bar
status = 'Tic-Tac-Toe'
label_header = Label(root,text=status,pady=7)
label_header.grid(row=0,column=0,columnspan=3)
#Buttons
button_1 = Button(root, text=t[0], width=8, height=4, command = lambda: gameplay(0)).grid(row=1,column=0)
button_2 = Button(root, text=t[1], width=8, height=4, command = lambda: gameplay(1)).grid(row=1,column=1)
button_3 = Button(root, text=t[2], width=8, height=4, command = lambda: gameplay(2)).grid(row=1,column=2)
button_4 = Button(root, text=t[3], width=8, height=4, command = lambda: gameplay(3)).grid(row=2,column=0)
button_5 = Button(root, text=t[4], width=8, height=4, command = lambda: gameplay(4)).grid(row=2,column=1)
button_6 = Button(root, text=t[5], width=8, height=4, command = lambda: gameplay(5)).grid(row=2,column=2)
button_7 = Button(root, text=t[6], width=8, height=4, command = lambda: gameplay(6)).grid(row=3,column=0)
button_8 = Button(root, text=t[7], width=8, height=4, command = lambda: gameplay(7)).grid(row=3,column=1)
button_9 = Button(root, text=t[8], width=8, height=4, command = lambda: gameplay(8)).grid(row=3,column=2)
#Information Bar
info = "Start Game"
label_header = Label(root,text=info,pady=7)
label_header.grid(row=4,column=0,columnspan=3)


root.mainloop()