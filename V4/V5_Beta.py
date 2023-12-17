# Evan Kupec's Final Project - SDEV140
# December 2023

import customtkinter as ctk
import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3

class left_side_scrl:
    def __init__(self, root):
        self.root = root
        self.root.title('customtkinter app')
        #self.root.geometry('600x400')

        # Create the main frame
        self.main_frame = ctk.CTkScrollableFrame(self.root, width=600)
        self.main_frame.pack(side=tk.LEFT)

        # Button to create nested frame
        self.create_frame_button = tk.Button(self.main_frame, text="Add Item", command=self.ask_for_item_number)
        self.create_frame_button.grid(row=0, column=6, padx=10, pady=5, sticky=tk.E)

        # Create Empty frame to fill space
        self.invisible_frame = ctk.CTkFrame(self.main_frame, width=400, height=1)
        self.invisible_frame.grid(row=0, column=0, padx=1, pady=1)

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

    def on_button_click(self, item_number, action_number):
        print(f"Item {item_number}, Action {action_number} clicked")

#-----------------------------------

def main():
    # Connect to the SQLite database (or create it if it doesn't exist)
    receipts_db = sqlite3.connect('receipts.db')

    # Create a cursor object to execute SQL commands
    c = receipts_db.cursor()

    # Create a table for receipts
    c.execute('''
        CREATE TABLE IF NOT EXISTS receipts (
            receipt_number INTEGER PRIMARY KEY,
            purchase_date DATE,
            customer_name TEXT
        )
    ''')

    # Create a table for items purchased
    c.execute('''
        CREATE TABLE IF NOT EXISTS items_purchased (
            item_id INTEGER PRIMARY KEY,
            receipt_number INTEGER,
            item_name TEXT,
            price REAL,
            FOREIGN KEY (receipt_number) REFERENCES receipts(receipt_number)
        )
    ''')

    # Commit the changes and close the connection
    receipts_db.commit()
    receipts_db.close()
    print("Database and tables created successfully.")


    root = ctk.CTk()
    ctk.set_appearance_mode("dark")

    app = left_side_scrl(root)
    root.mainloop()

if __name__ == "__main__":
    main()
