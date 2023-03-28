# I got this with the help of chatGPT. 
# adding something here for funsies

import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    # print("Username:", username)
    # print("Password:", password)

    if username == "admin" and password == "password":
        print("Login successful!") 
    else:
        print("Invalid username or password.")
        error_label.config(text="Invalid username or password.", fg="red")
    # You can add functionality to check the validity of the username and password here

# Create a new window
root = tk.Tk()
root.title("Login Page")

# Add a label for the username
username_label = tk.Label(root, text="Username:")
username_label.pack()

# Add an entry box for the username
username_entry = tk.Entry(root)
username_entry.pack()

# Add a label for the password
password_label = tk.Label(root, text="Password:")
password_label.pack()

# Add an entry box for the password
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Add a button to submit the login information
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# Add a label for error messages
error_label = tk.Label(root, text="")
error_label.pack()

# Start the event loop
root.mainloop()
