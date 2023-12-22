from tkinter import *
import time

def main():
    window = Tk()

    window.title("Farkle")
    window.geometry("1000x1000")
    window.configure(background = "white")
    window.resizable(width = False, height = False)

    roll_button = Button()

    window.mainloop()

main()