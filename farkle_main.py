from tkinter import *
import time
import die as di # die.py

global window

def select():
    print("button works")

def rolling_dice():
    di_list = []
    dibutton_list = []
    for i in range(0, 6):
        di_list.append(di.Die())
        print(di_list[i].number)
        dibutton_list.append(create_di(di_list[i]))
    return dibutton_list

def create_di(di):
    di_button = Button(window, command=select, height=80, width=80, bg='black')
    di_button.image = PhotoImage(file=("diface" + str(di.number) + ".png"))
    di_button.config(image=di_button.image, compound='top')
    di_button.pack()
    return di_button


def bank_score():
    pass #to be filled in later



window = Tk()

window.title("Farkle")
window.geometry("1000x1000")
window.configure(background = "#255c30")
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
                     padx=100
                    )
roll_button.pack(side=BOTTOM, pady=10)

bank_button = Button(window,
                    text="Bank",
                    command= bank_score,
                    font=('comic sans', 20),
                    bg="blue",
                    fg="white",
                    activebackground="blue",
                    activeforeground="white",
                    relief="raised",
                    bd=5,
                    padx=100
                    )
bank_button.pack(side=BOTTOM, pady=10)

roll_button.place(x=300, y=900)
bank_button.place(x=650, y=900)



window.mainloop()