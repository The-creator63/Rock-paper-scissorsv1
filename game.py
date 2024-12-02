from tkinter import*
import random
import tkinter.font as font

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("700x300")

heading_lbl = Label(root,text = "Rock Paper Scissors",font = font.Font(size = 20),fg = "black")
heading_lbl.pack()

winner_lbl = Label(root,text = "The game has begun",font = font.Font(size = 14),fg = "green")
winner_lbl.pack()

frame = Frame(root)
frame.pack()

options_lbl = Label(frame,text = "Your options: ",font = font.Font(size = 12),fg = "black")
options_lbl.grid(row = 0,column = 0)

root.mainloop()