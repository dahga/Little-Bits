import calendar
import tkinter as tk

class CalendarGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar")
        
        self.year = tk.StringVar()
        self.month = tk.StringVar()
        
        self.year.set(str(calendar.datetime.date.today().year))
        self.month.set(str(calendar.datetime.date.today().month))
        
        self.year.trace("w", self.update_calendar)
        self.month.trace("w", self.update_calendar)
        
        self.year_options = [str(i) for i in range(2010, 2030)]
        
        self.year_menu = tk.OptionMenu(self.master, self.year, *self.year_options)
        self.month_menu = tk.OptionMenu(self.master, self.month, *calendar.month_name[1:], command=self.update_calendar)
        
        self.prev_button = tk.Button(self.master, text="<<", command=self.prev_month)
        self.next_button = tk.Button(self.master, text=">>", command=self.next_month)
        
        self.calendar_label = tk.Label(self.master, font=("Arial", 14))
        
        self.year_menu.pack()
        self.month_menu.pack()
        self.prev_button.pack(side="left")
        self.next_button.pack(side="right")
        self.calendar_label.pack()
        
        self.update_calendar()
    
    def update_calendar(self, *args):
        year = int(self.year.get())
        try:
            month = list(calendar.month_name).index(self.month.get())
        except ValueError:
            month = int(self.month.get())
        
        calendar_str = calendar.month(year, month)
        
        self.calendar_label.config(text=calendar_str)
    
    def prev_month(self):
        current_month = self.month.get()
        if isinstance(current_month, int):
            if current_month == 1:
                self.month.set(12)
                self.year.set(str(int(self.year.get())-1))
            else:
                self.month.set(current_month - 1)
        else:
            month_num = list(calendar.month_name).index(current_month)
            if month_num == 1:
                self.month.set("December")
                self.year.set(str(int(self.year.get())-1))
            else:
                self.month.set(calendar.month_name[month_num-1])
        self.update_calendar()
    
    def next_month(self):
        current_month = self.month.get()
        if isinstance(current_month, int):
            if current_month == 12:
                self.month.set(1)
                self.year.set(str(int(self.year.get())+1))
            else:
                self.month.set(current_month + 1)
        else:
            month_num = list(calendar.month_name).index(current_month)
            if month_num == 12:
                self.month.set("January")
                self.year.set(str(int(self.year.get())+1))
            else:
                self.month.set(calendar.month_name[month_num+1])
        self.update_calendar()

root = tk.Tk()
gui = CalendarGUI(root)
root.mainloop()
