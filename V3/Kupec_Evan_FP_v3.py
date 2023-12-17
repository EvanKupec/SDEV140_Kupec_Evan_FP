#Evan Kupec's Final Project - SDEV140
#December 2023

#importing versions of tkinter and sqlite database
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

#-----------------------------------

#sets color theme, window name, and size
root = ctk.CTk()
ctk.set_appearance_mode("dark")
root.title('customtkinter app')
root.geometry('600x400')

#-----------------------------------
item_number = 0
#-----------------------------------

def ask_for_item_number(self):
    item_number = simpledialog.askstring("Item Number", "Enter the item number:")
    if item_number and item_number.isdigit():
        self.create_nested_frame(item_number)
    else:
        messagebox.showerror("Error", "Please enter a valid item number.")

def create_nested_frame(self, item_number):
    # Create a nested frame within the main frame
    nested_frame = ctk.CTkFrame(self.main_frame)
    nested_frame.grid(row=int(item_number), column=0, padx=20, pady=20)

    # Label above the buttons
    label = tk.Label(nested_frame, text=f"Item {item_number}")
    label.grid(row=0, column=0, columnspan=3)

    # Create three buttons within the nested frame
    button1 = tk.Button(nested_frame, text="Action 1", command=lambda: self.on_button_click(item_number, 1))
    button1.grid(row=1, column=0, padx=10, pady=5)

"""def button_test():
    print("button pressed")

def get_input():
    dialog = ctk.CTkInputDialog(text="Type in a number:", title="Test")
    user_num = dialog.get_input()
    print("Number:", user_num)

def trying_windows():
    messagebox.askquestion('Title', 'Body')

def create_window():
    extra_window = ctk.CTkToplevel()
    extra_window.title('Hello New Window')"""

def query_print():
    retail_db = sqlite3.connect("receipts.db")
    c = retail_db.cursor()
    c.execute("SELECT * FROM purchases")
    forprint = c.fetchall()
    print(forprint)

#-----------------------------------

#create/access sqlite "database"
retail_db = sqlite3.connect("receipts.db")
c = retail_db.cursor()

#c.execute("CREATE TABLE purchases (receipt_num integer, date text, dpci integer)")
#c.execute("INSERT INTO purchases VALUES ('43672', '12-14-2023', '207160018')")

retail_db.commit()
retail_db.close()

#-----------------------------------

scrl_left_frame = ctk.CTkScrollableFrame(root, width=500)
scrl_left_frame.pack(side=tk.LEFT)

nested_frame = ctk.CTkFrame(scrl_left_frame, border_width=5, border_color="red")
nested_frame.pack()

item_label = ctk.CTkLabel(nested_frame, text=item_number)

remove_item_button = tk.Button(nested_frame, text="Remove")
remove_item_button.pack(side=tk.LEFT)

create_nested_frame_button = ctk.CTkButton(root, command=ask_for_item_number, text="Create Frame")
create_nested_frame_button.pack(side=tk.RIGHT)

#-----------------------------------

#initiate main loop/start the program
root.mainloop()