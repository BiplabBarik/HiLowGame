##############################################################################
############### Hi Low Card Game based on Python Tkinter GUI #################
############### Author : Biplab Barik                        #################
############### Date   : Sep 2020                            #################
##############################################################################


from tkinter import *
from PIL import ImageTk,Image
import random

###################### CARD Faces ############################################
card_paths = [
          'Resources/CardFaces/AC.jpg','Resources/CardFaces/AD.jpg','Resources/CardFaces/AH.jpg','Resources/CardFaces/AS.jpg',
          'Resources/CardFaces/2C.jpg','Resources/CardFaces/2D.jpg','Resources/CardFaces/2H.jpg','Resources/CardFaces/2S.jpg',
          'Resources/CardFaces/3C.jpg','Resources/CardFaces/3D.jpg','Resources/CardFaces/3H.jpg','Resources/CardFaces/3S.jpg',
          'Resources/CardFaces/4C.jpg','Resources/CardFaces/4D.jpg','Resources/CardFaces/4H.jpg','Resources/CardFaces/4S.jpg',
          'Resources/CardFaces/5C.jpg','Resources/CardFaces/5D.jpg','Resources/CardFaces/5H.jpg','Resources/CardFaces/5S.jpg',
          'Resources/CardFaces/6C.jpg','Resources/CardFaces/6D.jpg','Resources/CardFaces/6H.jpg','Resources/CardFaces/6S.jpg',
          'Resources/CardFaces/7C.jpg','Resources/CardFaces/7D.jpg','Resources/CardFaces/7H.jpg','Resources/CardFaces/7S.jpg',
          'Resources/CardFaces/8C.jpg','Resources/CardFaces/8D.jpg','Resources/CardFaces/8H.jpg','Resources/CardFaces/8S.jpg',
          'Resources/CardFaces/9C.jpg','Resources/CardFaces/9D.jpg','Resources/CardFaces/9H.jpg','Resources/CardFaces/9S.jpg',
          'Resources/CardFaces/10C.jpg','Resources/CardFaces/10D.jpg','Resources/CardFaces/10H.jpg','Resources/CardFaces/10S.jpg',
          'Resources/CardFaces/JC.jpg','Resources/CardFaces/JD.jpg','Resources/CardFaces/JH.jpg','Resources/CardFaces/JS.jpg',
          'Resources/CardFaces/QC.jpg','Resources/CardFaces/QD.jpg','Resources/CardFaces/QH.jpg','Resources/CardFaces/QS.jpg',
          'Resources/CardFaces/KC.jpg','Resources/CardFaces/KD.jpg','Resources/CardFaces/KH.jpg','Resources/CardFaces/KS.jpg',
     ]

###################### Back Faces ############################################
back_paths = [
          'Resources/BackFaces/blue_back.jpg',
          'Resources/BackFaces/Gray_back.jpg',
          'Resources/BackFaces/Green_back.jpg',
          'Resources/BackFaces/purple_back.jpg',
          'Resources/BackFaces/Red_back.jpg',
          'Resources/BackFaces/Yellow_back.jpg',
     ]

#Background
main_bakg_path = 'Resources/Background/Background2.png'
main_icon_path = 'Resources/Icon/steam_tray.ico'


def GenerateRandom(x,y):
     return random.randint(x,y)

######################   Game UI  ############################################

GameWindow = Tk()
GameWindow.title("Hi Low Game Version 0.1")
GameWindow.geometry("500x500+100+100")
#GameWindow.resizable(FALSE,FALSE)
GameWindow.iconbitmap(main_icon_path)

BackgroundImage = Image.open(main_bakg_path)
BackgroundImage = BackgroundImage.resize((500, 500), Image.ANTIALIAS)
P_BackImage = ImageTk.PhotoImage(BackgroundImage)
BackGLabel  = Label(GameWindow, image=P_BackImage, borderwidth=0)
BackGLabel.pack(fill='both', expand=TRUE)

BackGLabel.rowconfigure(0, weight=50)
BackGLabel.rowconfigure(1, weight=200)
BackGLabel.rowconfigure(2, weight=200)
BackGLabel.rowconfigure(3, weight=50)
BackGLabel.columnconfigure(0, weight=50)
BackGLabel.columnconfigure(1, weight=200)

static_label_comp = Label(BackGLabel,text="Computer's Pick",font=("Helvetica", 12,"bold"),fg="#324aa8",bg='#f9f9f9')
static_label_comp.grid(row = 0, column = 0 , padx = 10 , pady = 2)

#Computer Card Init
back_card_id = GenerateRandom(0,5)
comp_card_id = back_card_id
comp_card_iamge = Image.open(back_paths[comp_card_id])
comp_card_iamge = comp_card_iamge.resize((140, 220), Image.ANTIALIAS)
computer_card = ImageTk.PhotoImage(comp_card_iamge)
comp_label = Label(BackGLabel, image=computer_card, borderwidth=0)
comp_label.grid(row = 1, column = 0 , padx = 2 , pady = 5)

#Player Card Init
plyr_card_id = back_card_id
plyr_card_iamge = Image.open(back_paths[plyr_card_id])
plyr_card_iamge = plyr_card_iamge.resize((140, 220), Image.ANTIALIAS)
player_card_back = ImageTk.PhotoImage(plyr_card_iamge)
plyr_label = Label(BackGLabel,image=player_card_back,borderwidth=0)
plyr_label.grid(row = 2, column = 0,padx = 2 , pady = 5)

static_label_plyr = Label(BackGLabel,text="Your Pick",font=("Helvetica", 12,"bold"),fg="#324aa8")
static_label_plyr.grid(row = 3, column = 0 , padx = 10 , pady = 5)


#Result Section
result_label = Label(BackGLabel,text="Result",font=("Helvetica", 12,"bold"),fg="#324aa8",bg='#f9f9f9')
result_label.place(x=300,y=20,width=100,height=20)

result_text = Label(BackGLabel,text="Select one Option",font=("Helvetica", 14,),fg="grey",bg='#f8f9f9')
result_text.configure(relief=GROOVE)
result_text.place(x=250,y=50,width=200,height=60)

#Buttons
shuf_button = Button(BackGLabel,text="Shuffle Deck",font=("Helvetica", 11,"bold"), padx=5,pady=5,fg="green")
shuf_button.place(x=275,y=200,width=150,height=40);

start_button = Button(BackGLabel,text="Start Game",font=("Helvetica", 11,"bold"), padx=5,pady=5,fg="green")
start_button.place(x=275,y=250,width=150,height=40);

pick_button = Button(BackGLabel,text="Pick a Card",font=("Helvetica", 11,"bold"), padx=5,pady=5,fg="green",state=DISABLED)
pick_button.place(x=275,y=300,width=150,height=40);

reset_button = Button(BackGLabel,text="Reset Game",font=("Helvetica", 11,"bold"), padx=5,pady=5,fg="green")
reset_button.place(x=275,y=400,width=150,height=40);

##############################################################################

def IsPlayerWon(plyr_pick,comp_pick):
     return TRUE
     
     
def Shuffle():
     global comp_card_id
     comp_card_id = GenerateRandom(0,51)
     result_text.configure(text="Deck Shuffled",fg="black")
     global computer_card
     plyr_label.configure(image=computer_card)
     comp_label.configure(image=computer_card)
     pick_button.configure(state=DISABLED)
     

def Start():
     global comp_card_id
     comp_card_id = GenerateRandom(0,51)
     comp_card_iamge = Image.open(card_paths[comp_card_id])
     comp_card_iamge = comp_card_iamge.resize((140, 220), Image.ANTIALIAS)
     computer_card = ImageTk.PhotoImage(comp_card_iamge)
     comp_label.configure(image=computer_card)
     comp_label.image = computer_card
     
     pick_button.configure(state=NORMAL)
     global player_card_back
     plyr_label.configure(image=player_card_back)
     plyr_label.image = player_card_back
     
     result_text.configure(text="Computer Picked",fg="black")

def Pick():
     global plyr_card_id
     global comp_card_id
     plyr_card_id = GenerateRandom(0,51)
     while plyr_card_id == comp_card_id :
          plyr_card_id = GenerateRandom(0,51)
     
     
     plyr_card_iamge = Image.open(card_paths[plyr_card_id])
     plyr_card_iamge = plyr_card_iamge.resize((140, 220), Image.ANTIALIAS)
     player_card = ImageTk.PhotoImage(plyr_card_iamge)
     plyr_label.configure(image=player_card)
     plyr_label.image = player_card
     
     if(comp_card_id > plyr_card_id):
          result_text.configure(text="You Lost !!",fg="red")
     else:
          result_text.configure(text="You Won !!",fg="green")
     
     pick_button.configure(state=DISABLED)
     
def Reset():
     global computer_card
     plyr_label.configure(image=computer_card)
     comp_label.configure(image=computer_card)
     pick_button.configure(state=DISABLED)
     result_text.configure(text="Select one Option",fg="black")
     
     
shuf_button.configure(command=Shuffle)
start_button.configure(command=Start)
pick_button.configure(command=Pick)
reset_button.configure(command=Reset)

########################### MAINLOOP #########################################
GameWindow.mainloop()