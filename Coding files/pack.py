import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import sqlite3


# Create a new window for the login page
def login_window():
    # Create a new window
    login_root = tk.Tk()
    login_root.title("Login")

    # Create a frame for the inputs
    frame = ttk.Frame(login_root, padding="20 20 20 20")
    frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    # Create a label and entry for the username
    ttk.Label(frame, text="Username: ").grid(column=0, row=0, sticky=tk.W)
    username_entry = ttk.Entry(frame)
    username_entry.grid(column=1, row=0, sticky=tk.W)

    # Create a label and entry for the password
    ttk.Label(frame, text="Password: ").grid(column=0, row=1, sticky=tk.W)
    password_entry = ttk.Entry(frame, show="*")
    password_entry.grid(column=1, row=1, sticky=tk.W)

    # Define a function for checking the login
    def check_login():
        # Get the values from the entries
        username = username_entry.get()
        password = password_entry.get()

        # Open a connection to the database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # Check if the username and password match
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()

        # Close the connection to the database
        conn.close()

        # If the user is found, close the login window and open the calendar window
        if user is not None:
            login_root.destroy()
            calendar_window()
        # If the user is not found, show an error message
        else:
            messagebox.showerror("Invalid Login", "Invalid username or password")

    # Create a button for checking the login
    ttk.Button(frame, text="Login", command=check_login).grid(column=1, row=2)

    # Start the mainloop for the login window
    login_root.mainloop()

# Create a new window for the calendar page
def calendar_window():
    # Create a new window
    root = tk.Tk()
    root.title("Calendar")

    # Create a frame for the inputs
    frame = ttk.Frame(root, padding="20 20 20 20")
    frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    # Create a label and entry for the title
    ttk.Label(frame, text="Title: ").grid(column=0, row=0, sticky=tk.W)
    title_entry = ttk.Entry(frame)
    title_entry.grid(column=1, row=0, sticky=tk.W)

    # Create a label and entry for the date
    ttk.Label(frame, text="Date: ").grid(column=0, row=1, sticky=tk.W)
    date_entry = ttk.Entry(frame)
    date_entry.grid(column=1, row=1, sticky=tk.W)
    date_entry.insert(0, datetime)
