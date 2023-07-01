BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
window = Tk()
window.configure(padx= 50, pady= 50, bg= BACKGROUND_COLOR)
#--------------------------Commands---------------------------#

#Try Except error to make sure that if there isnt a pre-existing file called words_to_learn, then it pulls from main file
try:
    data = pandas.read_csv('Day 31/flash-card-project-start/words_to_learn.csv')
    data = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("Day 31/flash-card-project-start/data/french_words.csv")
    data = data.to_dict(orient="records")



def clicked_button():
    global flip_timer, pick

    #cancel any flip_timer functions happening
    window.after_cancel(flip_timer)
    #creating pick and word variable
    pick = random.choice(data)
    word = pick['French']
    #configuring the card
    card.itemconfig(lang, text = "French", fill = 'black')
    card.itemconfig(card_image, image = frontphoto)
    card.itemconfig(diction, text= word, fill = 'black')
    #Flip the card
    flip_timer = window.after(3000, flip)
    

def clicked_right():
    global pick

    #call click function
    clicked_button()
    #Remove line from data
    data.remove(pick)
    #This line is to make sure it is running smoothly
    #print(len(data))

    #create to learn file
    to_learn = pandas.DataFrame.from_dict(data)
    to_learn = to_learn.to_csv("Day 31/flash-card-project-start/words_to_learn.csv", index=False)




def flip():
    global pick
    card.itemconfig(card_image, image = backphoto)
    word = pick['English']
    card.itemconfig(lang, text = "English", fill = 'white')
    card.itemconfig(diction, text= word, fill = 'white')

#Needed to not break. Could use try, except but im too lazy
flip_timer = window.after(3000, flip)
#-----------------------------UI-------------------------------#
#Everything below is just UI Creation, No special notes needed
wrongphoto = PhotoImage(file = "Day 31/flash-card-project-start/images/wrong.png")
wrong = Button(width= 100, height= 100, highlightthickness= 0, image= wrongphoto, command= clicked_button)
wrong.grid(column= 0, row= 1)

rightphoto = PhotoImage(file = "Day 31/flash-card-project-start/images/right.png")
right = Button(width= 100, height= 100, highlightthickness= 0, image=rightphoto, command= clicked_right)
right.grid(column=1, row=1)


backphoto = PhotoImage(file = "Day 31/flash-card-project-start/images/card_back.png")
frontphoto = PhotoImage(file = "Day 31/flash-card-project-start/images/card_front.png")

card = Canvas(width= 800, height= 526, highlightthickness= 0, bg = BACKGROUND_COLOR)
card_image = card.create_image(400, 263, image = frontphoto)
card.grid(column= 0, row= 0, columnspan= 2)
lang = card.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
diction = card.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))



window.mainloop()

