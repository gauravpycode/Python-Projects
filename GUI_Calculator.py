from tkinter import *
from customtkinter import *

root = CTk(fg_color="#212121")
root.title("Calculator")
root.geometry("590x720")
root.resizable(False, False)

font = ("Raleway", 20)
font2 = ("Raleway", 30)


def enter_number(num):
    entry.insert(INSERT, num)

def add():
    global operator, num1
    operator = "+"
    num1 = entry.get()
    entry.delete(0, END)

def multiply():
    global operator, num1
    operator = "*"
    num1 = entry.get()
    entry.delete(0, END)

def subtract():
    global operator, num1
    operator = "-"
    num1 = entry.get()
    entry.delete(0, END)

def divide():
    global operator, num1
    operator = "/"
    num1 = entry.get()
    entry.delete(0, END)

def modulus():
    global operator, num1
    operator = "%"
    num1 = entry.get()
    entry.delete(0, END)

def equal():
    global operator, num1
    num2 = entry.get()
    if operator == "+":
        result = float(num1) + float(num2)
        input_label.configure(text=f"{num1} + {num2}")
    elif operator == "-":
        result = float(num1) - float(num2)
        input_label.configure(text=f"{num1} - {num2}")
    elif operator == "*":
        result = float(num1) * float(num2)
        input_label.configure(text=f"{num1} * {num2}")
    elif operator == "/":
        result = float(num1) / float(num2)
        input_label.configure(text=f"{num1} / {num2}")
    elif operator == "%":
        result = float(num1) % float(num2)
        input_label.configure(text=f"{num1} % {num2}")
    entry.delete(0, END)
    entry.insert(0, result)

def clear_all():
    entry.delete(0, END)

def clear():
    num_length = len(entry.get())
    entry.delete(num_length-1)

def apply_color(color):
    divide_btn.configure(fg_color=color)
    multiply_btn.configure(fg_color=color)
    add_btn.configure(fg_color=color)
    minus_btn.configure(fg_color=color)
    equal_btn.configure(fg_color=color)

def apply_settings():
    global theme_choice
    theme = theme_choice.get()
    if theme == "Red":
        apply_color("#e53834")
    elif theme == "Pink":
        apply_color("#d81b60")
    elif theme == "Light-Green":
        apply_color("#7db242")
    elif theme == "Dark-Green":
        apply_color("#42a046")
    elif theme == "Teal":
        apply_color("#00887a")
    elif theme == "Orange":
        apply_color("#f5501e")
    elif theme == "Brown":
        apply_color("#6d4d40")
    elif theme == "Grey":
        apply_color("#546f7b")
    elif theme == "Black":
        apply_color("#333232")
    elif theme == "Purple":
        apply_color("#8e25ab")
    elif theme == "Dark-Purple":
        apply_color("#5e35b1")
    elif theme == "Blue":
        apply_color("#029ae5")
    elif theme == "Dark-Blue":
        apply_color("#3848ab")
    elif theme == "Yellow":
        apply_color("#fcd935")
    elif theme == "Golden":
        apply_color("#fa8c01")

def settings():
    global theme_choice
    setting_win = CTkToplevel(root)
    setting_win.geometry("800x600")
    setting_win.title("Settings")
    setting_win.resizable(False, False)

    frame = CTkFrame(setting_win, height=558, width=760, corner_radius=30)
    frame.place(x=20, y=20)

    head_label = CTkLabel(frame, text="Settings", font=("Raleway", 25))
    head_label.place(x=335, y=20)

    theme_label = CTkLabel(frame, text="Theme", font=("Raleway", 20))
    theme_label.place(x=20, y=120)

    theme_choice = CTkOptionMenu(frame, values=["Red", "Purple", "Dark-Purple", "Blue", "Dark-Blue", "Pink", "Orange", "Yellow", "Golden", "Teal", "Green", "Dark-Green", "Brown", "Grey", "Black"], font=("Raleway", 17), corner_radius=20)
    theme_choice.place(x=130, y=120)

    apply_btn = CTkButton(setting_win, text="Apply", font=("Raleway", 20), width=300, height=50, corner_radius=15, command=lambda: apply_settings())
    apply_btn.place(x=270, y=450)

    setting_win.mainloop()

menu_btn = CTkButton(root, text="...", font=font, width=20, fg_color="#212121", command=lambda: settings(), hover_color="#212121")
menu_btn.place(x=540, y=5)

input_label = CTkLabel(root, text="", font=font2)
input_label.place(x=20, y=60)

entry = CTkEntry(root, placeholder_text="0", font=font2, width=550, height=80, fg_color="#212121", border_color="#212121")
entry.place(x=20, y=130)

# row1

ac_btn = CTkButton(root, text="AC", font=font, height=80, width=120, corner_radius=20, fg_color="#6f6f6f", command=lambda: clear_all())
ac_btn.place(x=20, y=230)

clear_btn = CTkButton(root, text="C", font=font, height=80, width=120, corner_radius=20, fg_color="#6f6f6f", command=lambda: clear())
clear_btn.place(x=163, y=230)

modulus_btn = CTkButton(root, text="%", font=font, height=80, width=120, corner_radius=20, fg_color="#6f6f6f", command=lambda: modulus())
modulus_btn.place(x=306, y=230)

divide_btn = CTkButton(root, text="/", font=font, height=80, width=120, corner_radius=20, fg_color="#00887a", command=lambda: divide())
divide_btn.place(x=449, y=230)


# row2

seven_btn = CTkButton(root, text="7", font=font, height=80, width=120, corner_radius=20, fg_color="#3b3a3a", command=lambda: enter_number("7"))
seven_btn.place(x=20, y=330)

eight_btn = CTkButton(root, text="8", font=font, height=80, width=120, corner_radius=20, fg_color="#3b3a3a", command=lambda: enter_number("8"))
eight_btn.place(x=163, y=330)

nine_btn = CTkButton(root, text="9", font=font, height=80, width=120, corner_radius=20, fg_color="#3b3a3a", command=lambda: enter_number("9"))
nine_btn.place(x=306, y=330)

multiply_btn = CTkButton(root, text="*", font=font, height=80, width=120, corner_radius=20, fg_color="#00887a", command=lambda: multiply())
multiply_btn.place(x=449, y=330)


# row3

four_btn = CTkButton(root, text="4", font=font, height=80, width=120, corner_radius=20, fg_color="#3b3a3a", command=lambda: enter_number("4"))
four_btn.place(x=20, y=430)

five_btn = CTkButton(root, text="5", font=font, height=80, width=120, corner_radius=20, fg_color="#3b3a3a", command=lambda: enter_number("5"))
five_btn.place(x=163, y=430)

six_btn = CTkButton(root, text="6", font=font, height=80, width=120, corner_radius=20, fg_color="#3b3a3a", command=lambda: enter_number("6"))
six_btn.place(x=306, y=430)

minus_btn = CTkButton(root, text="-", font=font, height=80, width=120, corner_radius=20, fg_color="#00887a", command=lambda: subtract())
minus_btn.place(x=449, y=430)


# row4

one_btn = CTkButton(root, text="1", font=font, height=80, width=120, corner_radius=20, fg_color="#3b3a3a", command=lambda: enter_number("1"))
one_btn.place(x=20, y=530)

two_btn = CTkButton(root, text="2", font=font, height=80, width=120, corner_radius=20, fg_color="#3b3a3a", command=lambda: enter_number("2"))
two_btn.place(x=163, y=530)

three_btn = CTkButton(root, text="3", font=font, height=80, width=120, corner_radius=20, fg_color="#3b3a3a", command=lambda: enter_number("3"))
three_btn.place(x=306, y=530)

add_btn = CTkButton(root, text="+", font=font, height=80, width=120, corner_radius=20, fg_color="#00887a", command=lambda: add())
add_btn.place(x=449, y=530)


# row5

zero_btn = CTkButton(root, text="0", font=font, height=80, width=262, corner_radius=20, fg_color="#3b3a3a", command=lambda: enter_number("0"))
zero_btn.place(x=20, y=630)

dot_btn = CTkButton(root, text=".", font=font, height=80, width=120, corner_radius=20, fg_color="#3b3a3a", command=lambda: enter_number("."))
dot_btn.place(x=306, y=630)

equal_btn = CTkButton(root, text="=", font=font, height=80, width=120, corner_radius=20, fg_color="#00887a", command=lambda: equal())
equal_btn.place(x=449, y=630)


root.mainloop()