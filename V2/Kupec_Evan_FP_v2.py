import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import sqlite3

#-----------------------------------

window = ctk.CTk()
ctk.set_appearance_mode("dark")
window.title('customtkinter app')
window.geometry('600x400')

#-----------------------------------

def button_test():
    print("button pressed")

def get_input():
    dialog = ctk.CTkInputDialog(text="Type in a number:", title="Test")
    user_num = dialog.get_input()
    print("Number:", user_num)

def trying_windows():
    messagebox.askquestion('Title', 'Body')

def create_window():
    extra_window = ctk.CTkToplevel()
    extra_window.title('Hello New Window')

def query_print():
    retail_db = sqlite3.connect("receipts.db")
    c = retail_db.cursor()
    c.execute("SELECT * FROM purchases")
    forprint = c.fetchall()
    print(forprint)

#-----------------------------------

retail_db = sqlite3.connect("receipts.db")
c = retail_db.cursor()

#c.execute("CREATE TABLE purchases (receipt_num integer, date text, dpci integer)")
#c.execute("INSERT INTO purchases VALUES ('43672', '12-14-2023', '207160018')")

retail_db.commit()
retail_db.close()

#-----------------------------------

frame = ctk.CTkFrame(window, width=200, height=200, border_width=2, border_color='green')
frame.grid(column=0, row=0, columnspan=4, rowspan=5, padx=4, pady=2)

button1 = ctk.CTkButton(window, text="1 Yes No", command=trying_windows)
button1.grid(column=5, row=0)
button2 = ctk.CTkButton(window, text="2 Query Print", command=query_print)
button2.grid(column=5, row=1)
button3 = ctk.CTkButton(window, text="3 Create Window", command=create_window)
button3.grid(column=5, row=2)
button4 = ctk.CTkButton(window, text="4", command=button_test)
button4.grid(column=5, row=3)
button5 = ctk.CTkButton(window, text="5 Num Input", command=get_input)
button5.grid(column=5, row=4)

#-----------------------------------

window.mainloop()