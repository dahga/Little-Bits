from tkinter import *
from tkcalendar import *

root = Tk()
root.title('Little-Bits')
root.geometry("600x400")
root.resizable(0, 0)

header_frame = Frame(root)
entry_frame = Frame(root)
result_frame = Frame(root)
button_frame = Frame(root)

header_frame.pack(expand=True, fill="both")
entry_frame.pack(expand=True, fill="both")
result_frame.pack(expand=True, fill="both")
button_frame.pack(expand=True, fill="both")



cal = Calendar(root, selectmode="day", year=2023, month=4, day=16 )
cal.pack(pady=20)

def grab_date():
    my_label.config(text="Date Picked: " + cal.get_date())


my_button = Button(root, text="Get Date",bg="#A020F0", fg="#E0FFFF", command = grab_date, font=('arial', '15'))
my_button.pack(pady=20)

my_label = Label(header_frame, text="CALENDAR", font=('arial', '25', 'bold'), fg="#A020F0")
my_label.pack(expand=True, fill="both")
root.mainloop()