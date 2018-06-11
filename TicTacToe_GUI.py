from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
import time

#Global Variables
activePlayer=1
p1=[]   #what player 1 selected
p2=[]   #what player 2 selected

root=Tk()
root.geometry("450x450+0+0")
root.title("Tic Tac Toe Game")

s=ttk.Style()
s.theme_use('winnative')

tops=Frame(root,width=400, height=50, bg="sky blue",relief=SUNKEN)
tops.pack(side=TOP)

fr=Frame(root,width=500, height=400,relief=SUNKEN)
fr.pack(side=TOP)

#===========================info===============================================
local_time=time.asctime(time.localtime(time.time()))

Label_info=Label(tops,font=('arial',20, 'bold'), text='Tic Tac Toe Game', fg='steel blue',bd=10,anchor='w')
Label_info.grid(row=0,column=0)

Label_info=Label(tops,font=('arial',10,'bold'), text='Player 1 is X\nPlayer 2 is O', fg='steel blue',bd=10,anchor='w')
Label_info.grid(row=1,column=0)

#==========================Add buttons==========================================
bu1=ttk.Button(fr,text=' ')
bu1.grid(row=0,column=0, sticky='snew',ipadx=30,ipady=30)
bu1.config(command=lambda :buttonClick(1))

bu2=ttk.Button(fr,text=' ')
bu2.grid(row=0,column=1, sticky='snew',ipadx=30,ipady=30)
bu2.config(command=lambda :buttonClick(2))

bu3=ttk.Button(fr,text=' ')
bu3.grid(row=0,column=2, sticky='snew',ipadx=30,ipady=30)
bu3.config(command=lambda :buttonClick(3))

bu4=ttk.Button(fr,text=' ')
bu4.grid(row=1,column=0, sticky='snew',ipadx=30,ipady=30)
bu4.config(command=lambda :buttonClick(4))

bu5=ttk.Button(fr,text=' ')
bu5.grid(row=1,column=1, sticky='snew',ipadx=30,ipady=30)
bu5.config(command=lambda :buttonClick(5))

bu6=ttk.Button(fr,text=' ')
bu6.grid(row=1,column=2, sticky='snew',ipadx=30,ipady=30)
bu6.config(command=lambda :buttonClick(6))

bu7=ttk.Button(fr,text=' ')
bu7.grid(row=2,column=0, sticky='snew',ipadx=30,ipady=30)
bu7.config(command=lambda :buttonClick(7))

bu8=ttk.Button(fr,text=' ')
bu8.grid(row=2,column=1, sticky='snew',ipadx=30,ipady=30)
bu8.config(command=lambda :buttonClick(8))

bu9=ttk.Button(fr,text=' ')
bu9.grid(row=2,column=2, sticky='snew',ipadx=30,ipady=30)
bu9.config(command=lambda :buttonClick(9))

def buttonClick(id):
    global activePlayer
    global p1, p2
    if activePlayer==1:
        setLayer(id,"X")
        p1.append(id)
        root.title("Tic Tac Toe Game: player 2 your turn")
        activePlayer=2
        print ("p1:{}".format(p1))
       # Autoplay()
    elif activePlayer==2:
        setLayer(id,"O")
        p2.append(id)
        root.title("Tic Tac Toe Game: player 1 your turn")
        activePlayer=1
        print ("p2{}".format(p2))
    checkWinner()
def qExit():
    root.destroy()

def Reset():
    global p1, p2
    setLayer(id,"")
    p1.set("")
    p2.set("")

    buttonClick(id)

def setLayer(id,playerSymbol):
    if id==1:
        bu1.config(text=playerSymbol)
        bu1.state(['disabled'])
    elif id==2:
        bu2.config(text=playerSymbol)
        bu2.state(['disabled'])
    elif id==3:
        bu3.config(text=playerSymbol)
        bu3.state(['disabled'])
    elif id==4:
        bu4.config(text=playerSymbol)
        bu4.state(['disabled'])
    elif id==5:
        bu5.config(text=playerSymbol)
        bu5.state(['disabled'])
    elif id==6:
        bu6.config(text=playerSymbol)
        bu6.state(['disabled'])
    elif id==7:
        bu7.config(text=playerSymbol)
        bu7.state(['disabled'])
    elif id==8:
        bu8.config(text=playerSymbol)
        bu8.state(['disabled'])
    elif id==9:
        bu9.config(text=playerSymbol)
        bu9.state(['disabled'])

def checkWinner():
    winner=-1
    if ((1 in p1) and (2 in p1) and (3 in p1)):
        winner=1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        winner=2

    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winner=1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winner=2

    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winner=1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winner=2

    if ((7 in p1) and (4 in p1) and (1 in p1)):
        winner=1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winner=2

    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winner=1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winner=2

    if ((7 in p1) and (5 in p1) and (3 in p1)):
        winner=1
    if ((7 in p2) and (5 in p2) and (3 in p2)):
        winner=2

    if ((8 in p1) and (5 in p1) and (2 in p1)):
        winner=1
    if ((8 in p2) and (5 in p2) and (2 in p2)):
        winner=2

    if ((9 in p1) and (6 in p1) and (3 in p1)):
        winner=1
    if ((9 in p2) and (6 in p2) and (3 in p2)):
        winner=2

    if winner==1:
        messagebox.showinfo(title="Congratulations Amigos!",message="Player 1 is the winner, Press Ok to exit")
      #  exit()
    elif winner==2:
        messagebox.showinfo(title="Congratulations Amigos!",message="Player 2 is the winner. Press Ok to exit")
       # exit()
    elif (len(p1)==5 or len(p2)==5):
        messagebox.showinfo(title="Result shown!",message="Unfortunately, It's a tie. Hit OK and play again")
        exit()

def Autoplay():
    emptyCells=[]
    global p1,p2
    for cell in range(9):
        if (not((cell+1 in p1) or (cell+1 in p2))):
            emptyCells.append(cell+1)
       # if len(emptyCells)<5:
            randomIndex=randint(0,len(emptyCells)-1)
            buttonClick(emptyCells[randomIndex])

btnExit=Button(fr, font=('Arial',10,'bold'),padx=16,pady=8,bg='powder blue', bd=16,fg='black',width=10,text='Exit',
                command=qExit).grid(row=3,column=2)
btnReset=Button(fr,font=('Arial',10,'bold'),padx=16,pady=8,bg='powder blue', bd=16,fg='black',width=10,text='Reset',
                command=Reset).grid(row=3,column=0)
root.mainloop()