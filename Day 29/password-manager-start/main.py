PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip
from tkinter import messagebox
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def pword_generator():
    pass_entry.delete(0, END)
    fin_pass = []
    for i in range (8):
        fin_pass.append(random.choice(letters))
    for i in range(4):
        fin_pass.append(random.choice(numbers))
    for i in range(2):
        fin_pass.append(random.choice(symbols))
    random.shuffle(fin_pass)
    fin_pass = "".join(fin_pass)
    pass_entry.insert(END, string= fin_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clicked_add():
     # Get input values
    web = web_entry.get()
    pword = pass_entry.get()
    em = email_entry.get()
    
    # Create new data entry
    new_data = {
        web: {
            "email": em,
            "password": pword
        }
    }
    
    # Check if any fields are empty
    if len(web) == 0 or len(pword) == 0 or len(em) == 0:
        messagebox.showinfo(title="OOPS!", message="Please don't leave any fields empty")
    else:
        try:
            # Read existing data from file
            with open("Day 29\password-manager-start\data.json", 'r') as file:
                data = json.load(file)
                # Update existing data with new data
                data.update(new_data)
        except FileNotFoundError:
            # Create a new file if it doesn't exist
            with open("Day 29\password-manager-start\data.json", 'w') as file:
                data = new_data
        
        # Save updated data to file
        with open("Day 29\password-manager-start\data.json", 'w') as file:
            json.dump(data, file, indent=4)
        
        # Clear input fields
        web_entry.delete(0, END)
        pass_entry.delete(0, END)
        email_entry.delete(0, END)
        
        # Copy password to clipboard
        pyperclip.copy(pword)
# -----------------------------Search------------------------------------------#
def search_it():
    web = web_entry.get()
    try:
        with open("Day 29\password-manager-start\data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title = "ERROR", message = "no directory showing")
    else:
        if web in data:
            info = data[web]
            u_name = info['email']
            pw = info['password']
            messagebox.showinfo(title= "Info", message = f"Email: {u_name} \nPassword: {pw}")
        else:
            messagebox.showinfo(title= "Error", message= f"No {web} in directory")

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.title("Password Generator")
window.config(padx = 100, pady = 20)

picture = Canvas(width = 200, height = 189)
image1 = PhotoImage(file ="Day 29/password-manager-start/logo.png")
picture.create_image(100, 94, image = image1)
picture.grid(row=0, column= 1)

website = Label(text = "Website:")
website.grid(row=1, column=0)

email = Label(text = "Email/Username:")
email.grid(row=2, column=0)

password = Label(text = "Password:")
password.grid(row=3, column=0)

web_entry = Entry()
web_entry.grid(row=1,column=1, columnspan= 2, sticky= 'we')

email_entry = Entry()
email_entry.insert(END, "dmccord9912@gmail.com")
email_entry.grid(row=2,column=1, columnspan= 2, sticky= 'we')

pass_entry = Entry()
pass_entry.grid(row=3,column=1, columnspan=2, sticky = 'we')

generate = Button(text="Generate Password", command= pword_generator)
generate.grid(row = 3, column= 2)

add = Button(text = "add", command= clicked_add)
add.grid(row = 4, column= 1, columnspan= 2, sticky= 'we')

search = Button(text = "search", command= search_it)
search.grid(row =1, column= 2, sticky= 'we')


window.mainloop()

