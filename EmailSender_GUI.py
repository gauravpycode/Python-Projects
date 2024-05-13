from tkinter import *
from customtkinter import *
from email.message import EmailMessage
import smtplib
from smtplib import SMTPAuthenticationError
import ssl
from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    speak_answer = gTTS(text=text)
    speak_answer.save("tmptext.mp3")
    playsound("tmptext.mp3")
    os.remove("tmptext.mp3")

set_default_color_theme("green")
set_appearance_mode("dark")

email_password = "lszpbjbmgacdlnhv"
email_sender = "darkpycode@gmail.com"

email_list = email_sender.split("@")
username = email_list[0]

def send_email():
    email_receiver = email_recevier_entry.get()
    email_subject = email_subject_entry.get()
    email_body = email_body_entry.textbox.get("1.0",END)

    try:
        if "@" in email_receiver and email_subject != "":
            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = email_receiver
            em["subject"] = email_subject
            em.set_content(email_body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
                error_label.configure(text="Email send successfully.")
                speak("Email send successfully.")
        elif email_subject == "":
            error_label.configure(text="Please fill the subject field.")
            speak("Please fill the subject field.")
        elif "@" not in email_receiver:
            error_label.configure(text="Invalid email format!")
            speak("Invalid email format!")
        else:
            error_label.configure(text="Some error occured please ensure that you fill all details correctly.")
            speak("Some error occured please ensure that you fill all details correctly.")
    except SMTPAuthenticationError:
        error_label.configure(text="No gmail account found with the given email.")
        speak("No gmail account found with the given email.")

root = CTk()
root.geometry("1000x900")
root.title("Email Sender")
root.resizable(False, False)

username_label = CTkLabel(root, text=f"Logged in as: {username}", font=("Raleway", 15))
username_label.place(x=10, y=10)

head_label = CTkLabel(root, text="Email Sender", font=("Raleway", 25))
head_label.place(x=450, y=40)

email_recevier_label = CTkLabel(root, text="Receiver's Email", font=("Raleway", 20))
email_recevier_label.place(x=150, y=160)

email_recevier_entry = CTkEntry(root, font=("Raleway", 20), width=450, height=50)
email_recevier_entry.place(x=450, y=150)

email_subject_label = CTkLabel(root, text="Email Subject", font=("Raleway", 20))
email_subject_label.place(x=150, y=260)

email_subject_entry = CTkEntry(root, font=("Raleway", 20), width=450, height=50)
email_subject_entry.place(x=450, y=250)

email_body_label = CTkLabel(root, text="Email Content", font=("Raleway", 20))
email_body_label.place(x=450, y=360)

email_body_entry = CTkTextbox(root, font=("Raleway", 20), width=760, height=290)
email_body_entry.place(x=150, y=450)

send_button = CTkButton(root, text="Send", font=("Raleway", 20), command=lambda:send_email(), width=200, corner_radius=15)
send_button.place(x=400, y=780)

error_label = CTkLabel(root, text="", font=("Raleway", 20))
error_label.place(x=50, y=850)

root.mainloop()
