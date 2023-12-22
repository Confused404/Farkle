from tkinter import *
import time

def rolling_dice():
    pass #to be filled in later

def main():
    window = Tk()

    window.title("Farkle")
    window.geometry("1000x1000")
    window.configure(background = "white")
    window.resizable(width = False, height = False)

    roll_button = Button(window,
                         text="Roll",
                         command= rolling_dice,
                         font=('comic sans', 20),
                         bg="red",
                         fg="white",
                         activebackground="red",
                         activeforeground="white",
                         relief="raised",
                         bd=5,
                        )
    roll_button.pack(side=LEFT, padx=5, pady=5)
    window.mainloop()

main()