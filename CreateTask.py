#All parts were made by me, unless specifically stated

from tkinter import *                   
import random
from tkinter import messagebox
from tkinter import ttk
#imports certain packages to display the GUI


frame = Tk()
frame.geometry("450x450")
frame.title("Shell Game")
frame.configure(background = 'pale turquoise')

#determines the dimensions and color of the window(made by my patner)

score = 500

#This is the initial score

def game():
        instructions()

#After pressing play, the player learns the instructions


def scoreBox(score):
        if score < 0:
                lose()
        elif score == 1000:
                win()
        messagebox.showinfo("Score", str(score))

#complex algorithm that determines whether the player has won/lost and displays score

def lose():
        messagebox.showinfo("Game Over!", "YOU LOSE!")

def win():
        messagebox.showinfo("YAY!", "YOU WIN!")

#function win and function lose let the player know they won/lost, respectively

def increasepts():
        global score
        score = score + 100
        scoreBox(score)
		
def decreasepts():
        global score
        score = score - 100
        scoreBox(score)

#increasepts and decreasepts update score
        
def instructions():
        messagebox.showinfo("Instructions", "Great! The objective of the game is to choose the correct shell.")

#These are the instructions

def btn1():
        num = random.randint(1, 4)
        if num == 1:
                increasepts()
        elif num != 1:
                decreasepts()

def btn2():
        num = random.randint(1, 4)
        if num == 2:
                increasepts()
        elif num != 2:
                decreasepts()

def btn3():
        num = random.randint(1, 4)
        if num == 3:
                increasepts()
        elif num != 3:
                decreasepts()

#btn1, btn2, bt3 generate random numbers when shell pressed(made by partner)

lbl1 = Label(width=30,height=10, text="Welcome to the Shell Game!", bg = 'pale turquoise', font=("Comic Sans ms", 11, "bold"))
lbl1.place(x=80, y=-40)

btn_play = Button(text="Play", width=19, height=2, bg = 'light goldenrod', font=("Comic Sans ms", 12), command=game)
btn_play.place(x = 117, y = 80)

lbl2 = Label(text="Press The Button Above To Begin", width=30, height=1)
lbl2.place(x = 109, y = 150)

btn_shell1 = Button(text="Shell 1",width=10, height=2, command=btn1)
btn_shell1.place(x = 95, y = 175)

btn_shell2 = Button(text="Shell 2", width=10, height=2, command=btn2)
btn_shell2.place(x = 175, y = 175)

btn_shell3 = Button(text="Shell 3", width=10, height=2, command=btn3)
btn_shell3.place(x = 255, y = 175)

#these are the buttons and labels(made by partner)

frame.mainloop()

#this loops the program



