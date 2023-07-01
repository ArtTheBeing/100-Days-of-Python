from tkinter import * #Imports everything from tkinter

window = Tk()

def m_to_km():
    x = float(input.get())
    x *= 1.60934
    x = round(x ,2)
    num.config(text = x)

window.title("Mile to Km Converter")
window.minsize(width=400,height=100)
window.config(padx= 50, pady = 20)

input = Entry(bg = "white")
input.insert(END, string = 0)
input.grid(column= 1, row = 0)

miles = Label()
miles.config(text= "Miles")
miles.grid(column= 2, row = 0)

is_equal_to = Label()
is_equal_to.config(text= "is equal to")
is_equal_to.grid(column= 0, row = 1)

num = Label()
num.config(text= 0)
num.grid(column= 1, row = 1)

km = Label()
km.config(text= "km")
km.grid(column= 2, row = 1)

calculate = Button(text = "Calculate", command = m_to_km)
calculate.grid(column= 1, row=2)

window.mainloop()