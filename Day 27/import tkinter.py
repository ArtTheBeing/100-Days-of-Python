from tkinter import * #Imports everything from tkinter

window = Tk()

window.title("First GUI program")
window.minsize(width=500,height=300)

#If want padding
window.config(padx = 100, pady = 200)

#Label

mylabel = Label(text = "I am a label", font = ("Arial", 24, "bold"))

#.pack() places the interface to the screen, and auto centers. Otherwise known as the "packer"
mylabel.grid(column= 0, row = 0)
mylabel.config(padx = 50, pady= 50)
#mylabel.pack(side = "left")
#mylabel.pack(expand = "True")


#Ways to change
mylabel["text"] = "New Text"
#or
mylabel.config(text = "New Text")


def button_clicked():
    mylabel.config(text = text.get())


#(command is what calls function. Kind of like screen listen onkey)
button = Button(text = "Click me", command = button_clicked)
button.grid(column= 1, row= 1)

button2 = Button(text = "button2")
button2.grid(column=2, row = 0)
#Entry

input = Entry(bg = "white")
input.grid(column= 3, row = 2)
text = Text(bg = "light blue")











window.mainloop()