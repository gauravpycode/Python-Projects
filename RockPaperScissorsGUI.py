from tkinter import *
from customtkinter import *
from PIL import Image
import random


global player_score
global computer_score
global player_score_label
global computer_score_label
global player_output
global computer_output
global possible_outcomes

possibe_outcomes = ["rock", "paper", "scissor"]

set_appearance_mode("dark")

root = CTk()
root.title("Rock Paper And Scissor Game")
root.geometry("1000x800")
root.resizable(False, False)

global stone2_image
global paper2_image
global scissor2_image
global player_label
global computer_label

player_score = 0
computer_score = 0

stone2_image = CTkImage(Image.open("/home/gaurav/Documents/Python/Projects 2.0/Images/stone3.png"), size=(250,350))
paper2_image = CTkImage(Image.open("/home/gaurav/Documents/Python/Projects 2.0/Images/paper3.png"), size=(250,350))
scissor2_image = CTkImage(Image.open("/home/gaurav/Documents/Python/Projects 2.0/Images/scissor3.png"), size=(250,350))
play_image = CTkImage(Image.open("/home/gaurav/Documents/Python/Projects 2.0/Images/play.png"), size=(250,350))


def reset():
    global computer_score, player_score
    player_score = 0
    computer_score = 0


def game():
    global player_score
    global computer_score
    global player_output
    global player_score_label
    global computer_score_label
    global player_label
    global computer_label
    
    computer_output = random.choice(possibe_outcomes)

    if player_output == computer_output:
        computer_score += 0
        player_score += 0
        
        player_score_label.configure(text=f"Player's Score: {player_score}")
        computer_score_label.configure(text=f"Computer's Score: {computer_score}")


        if computer_output == "rock":
            player_label.configure(image=stone2_image)
            computer_label.configure(image=stone2_image)
        
        elif computer_output == "paper":
            player_label.configure(image=paper2_image)
            computer_label.configure(image=paper2_image)
        
        elif computer_output == "scissor":
            player_label.configure(image=scissor2_image)
            computer_label.configure(image=scissor2_image)
            

    elif player_output == "rock" and computer_output == "paper":
        computer_score += 1
        player_label.configure(image=stone2_image)
        computer_label.configure(image=paper2_image)
        player_score_label.configure(text=f"Player's Score: {player_score}")
        computer_score_label.configure(text=f"Computer's Score: {computer_score}")
    
    elif player_output == "rock" and computer_output == "scissor":
        player_score += 1
        player_label.configure(image=stone2_image)
        computer_label.configure(image=scissor2_image)
        player_score_label.configure(text=f"Player's Score: {player_score}")
        computer_score_label.configure(text=f"Computer's Score: {computer_score}")

    elif player_output == "paper" and computer_output == "rock":
        player_score += 1
        player_label.configure(image=paper2_image)
        computer_label.configure(image=stone2_image)
        player_score_label.configure(text=f"Player's Score: {player_score}")
        computer_score_label.configure(text=f"Computer's Score: {computer_score}")
    
    elif player_output == "paper" and computer_output == "scissor":
        computer_score += 1
        player_label.configure(image=paper2_image)
        computer_label.configure(image=scissor2_image)
        player_score_label.configure(text=f"Player's Score: {player_score}")
        computer_score_label.configure(text=f"Computer's Score: {computer_score}")

    elif player_output == "scissor" and computer_output == "paper":
        player_score += 1
        player_label.configure(image=scissor2_image)
        computer_label.configure(image=paper2_image)
        player_score_label.configure(text=f"Player's Score: {player_score}")
        computer_score_label.configure(text=f"Computer's Score: {computer_score}")
    
    elif player_output == "scissor" and computer_output == "rock":
        computer_score += 1
        player_label.configure(image=scissor2_image)
        computer_label.configure(image=stone2_image)
        player_score_label.configure(text=f"Player's Score: {player_score}")
        computer_score_label.configure(text=f"Computer's Score: {computer_score}")

    if computer_score == 10 or player_score == 10:
        if computer_score == 10:
            label = CTkLabel(root, text="Computer Win!", font=("Raleway", 25))
            label.place(x=700, y=20)
            reset()
        else:
            label = CTkLabel(root, text="Player Win!", font=("Raleway", 25))
            label.place(x=700, y=20)
            reset()


def rock():
    global player_output
    player_output = "rock"
    game()


def paper():
    global player_output
    player_output = "paper"
    game()


def scissor():
    global player_output
    player_output = "scissor"
    game()



stone_image = CTkImage(Image.open("/home/gaurav/Documents/Python/Projects 2.0/Images/Stone2.png"), size=(120,120))
paper_image = CTkImage(Image.open("/home/gaurav/Documents/Python/Projects 2.0/Images/paper2.png"), size=(120,120))
scissor_image = CTkImage(Image.open("/home/gaurav/Documents/Python/Projects 2.0/Images/Scissor2.png"), size=(120,120))


frame = CTkFrame(root, width=960, height=760, corner_radius=50)
frame.place(x=20, y=20)

player_score_label = CTkLabel(frame, text=f"Player's Score: {player_score}", font=("Raleway", 15))
computer_score_label = CTkLabel(frame, text=f"Computer's Score: {computer_score}", font=("Raleway", 15))
player_score_label.place(x=250, y=50)
computer_score_label.place(x=250, y=100)

stone_btn = CTkButton(frame, height=0, width=0, corner_radius=20, image=stone_image, text="", fg_color="transparent", command=lambda: rock())
stone_btn.place(x=275, y=170)
paper_btn = CTkButton(frame, height=0, width=0, corner_radius=20, image=paper_image, text="", fg_color="transparent", command=lambda: paper())
paper_btn.place(x=425, y=170)
scissor_btn = CTkButton(frame, height=0, width=0, corner_radius=20, image=scissor_image, text="", fg_color="transparent", command=lambda: scissor())
scissor_btn.place(x=575, y=170)

cmp_label = CTkLabel(frame, text="Computer", font=("Raleway", 25))
player_label = CTkLabel(frame, text="Player", font=("Raleway", 25))
cmp_label.place(x=150, y=355)
player_label.place(x=730, y=355)

computer_label = CTkLabel(frame, image=play_image, text="")
computer_label.place(x=100, y=400)
player_label = CTkLabel(frame, image=play_image, text="")
player_label.place(x=650, y=400)

root.mainloop()
