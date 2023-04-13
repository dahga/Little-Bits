# I got this with the help of chatGPT. 
# adding something here for funsies

import tkinter as tk
import sqlite3

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
    else:
        print("Invalid username or password.")
        error_label.config(text="Invalid username or password.", fg="red")

    # Close the database connection
    conn.commit()
    conn.close()
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
