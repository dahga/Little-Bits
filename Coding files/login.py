# I got this with the help of chatGPT. 
# adding something here for funsies

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import sqlite3
from tkcalendar import *

def login():
    username = username_entry.get()
    password = password_entry.get()
    # print("Username:", username)
    # print("Password:", password)

    # Connect to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # creating a table 
    # c.execute(""" CREATE TABLE customers (
    #         username text,
    #         password text
    #     )""")

    # 3 users in the database for now 
    # c.execute("INSERT INTO customers VALUES ('Sally_student', 'MSUMSally!')")
    # c.execute("INSERT INTO customers VALUES ('Ashley_mom', 'busyMom101')")
    # c.execute("INSERT INTO customers VALUES ('Linda_business', 'itsmybusiness!!')")
    # c.execute("INSERT INTO customers VALUES ('user', 'pass!')")

    # checks to see what is in the database 
    c.execute("SELECT * FROM customers")
    print(c.fetchall())
    
    # conn.commit()

    # # Query the database for the user's login information
    c.execute("SELECT * FROM customers WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    # # Check if the user's login information is valid
    if user:
        print("Login successful!")
        error_label.config(text="")
        root.destroy()  # Close the login window
        show_calendar()  # Open the calendar window
    else:
        print("Invalid username or password.")
        error_label.config(text="Invalid username or password.", fg="red")

    # Close the database connection
    conn.commit()
    conn.close()
# Create a new window
root = tk.Tk()
root.title("Login Page")

root.geometry("550x600")

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

def show_calendar():
    # Create a GUI window
    cal_gui = tk.Tk()

    # Set the background colour of GUI window
    cal_gui.config(background="white")

    # set the name of tkinter GUI window
    cal_gui.title("CALENDAR")

    # Set the configuration of GUI window
    cal_gui.geometry("550x600")

    style = ttk.Style(cal_gui)
    style.theme_use('clam')

    header_frame = Frame(cal_gui)
    entry_frame = Frame(cal_gui)
    result_frame = Frame(cal_gui)
    button_frame = Frame(cal_gui)

    header_frame.pack(expand=True, fill="both")
    entry_frame.pack(expand=True, fill="both")
    result_frame.pack(expand=True, fill="both")
    button_frame.pack(expand=True, fill="both")

    cal = Calendar(cal_gui, selectmode="day", year=2023, month=4, day=16 )
    cal.pack(pady=20)

    def grab_date():
        my_label.config(text="Date Picked: " + cal.get_date())


    my_button = Button(cal_gui, text="Get Date",bg="#A020F0", fg="#448282", command = grab_date, font=('arial', '15'))
    my_button.pack(pady=20)

    my_label = Label(header_frame, text="CALENDAR", font=('arial', '25', 'bold'), fg="#448282")
    my_label.pack(expand=True, fill="both")


    def show_events():
        # something here
        root = tk.Tk()
        root.title("Add Event to Calendar")

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
        date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

        # Create a label and entry for the time
        ttk.Label(frame, text="Time: ").grid(column=0, row=2, sticky=tk.W)
        time_entry = ttk.Entry(frame)
        time_entry.grid(column=1, row=2, sticky=tk.W)
        time_entry.insert(0, datetime.today().strftime('%H:%M'))

        # Create a label and entry for the notes
        ttk.Label(frame, text="Notes: ").grid(column=0, row=3, sticky=tk.W)
        notes_entry = ttk.Entry(frame)
        notes_entry.grid(column=1, row=3, sticky=tk.W)
        # Define a function for adding the event
        def add_event():
            title = title_entry.get()
            date = date_entry.get()
            time = time_entry.get()
            notes = notes_entry.get()
            messagebox.showinfo("New Event Added", f"Title: {title}\nDate: {date}\nTime: {time}\nNotes: {notes}")
            # Clear the entries
            title_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))
            time_entry.delete(0, tk.END)
            time_entry.insert(0, datetime.today().strftime('%H:%M'))
            notes_entry.delete(0, tk.END)

        # Create a button for adding the event
        ttk.Button(frame, text="Add", command=add_event).grid(column=1, row=4, sticky=tk.W)


    add_event = Button(cal_gui, text="Add Event", bg="#A020F0", fg="#448282", command=show_events, font=('arial', '15'))
    add_event.pack()

    exit_button = Button(cal_gui, text = "Exit", bg="#A020F0", fg="#448282", command = exit, font=('arial', '15'))
    exit_button.pack()

    # Start the event loop for the new GUI window
    cal_gui.mainloop()

# Start the event loop
root.mainloop()
