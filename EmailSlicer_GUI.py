from tkinter import *
from customtkinter import *
from tkinter import messagebox

root = CTk()
root.geometry("700x500")
root.title("Email Slicer")

set_default_color_theme("blue")
set_appearance_mode("dark")

def slice_email():
    email = email_entry.get()
    email = email.split("@")
    name = email[0]
    domain = email[1]

    name_label = CTkLabel(root, text=f"Name: {name}", font=("Raleway", 15))
    name_label.place(x=250, y=350)

    domain_label = CTkLabel(root, text=f"Domain: {domain}", font=("Raleway", 15))
    domain_label.place(x=250, y=400)


head_label = CTkLabel(root, text="Email Slicer", font=("Raleway", 20))
head_label.place(x=250, y=25)

email_label = CTkLabel(root, text="Email Address", font=("Raleway", 15))
email_label.place(x=80, y=150)

email_entry = CTkEntry(root, font=("Raleway", 15), width=350)
email_entry.place(x=280, y=150)

submit_btn = CTkButton(root, text="Slice Email", width=350, command=lambda:slice_email())
submit_btn.place(x=180, y=250)



root.mainloop()
