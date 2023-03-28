import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

# Create a new window
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
ttk.Button(frame, text="Add Event", command=add_event).grid(column=1, row=4, sticky=tk.W)

# Run the main loop
root.mainloop()