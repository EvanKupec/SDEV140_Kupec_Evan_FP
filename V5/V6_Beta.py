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
        # self.root.geometry('600x400')
        self.row_index = 1

        # Create the main frame
        self.main_frame = ctk.CTkScrollableFrame(self.root, width=600)
        self.main_frame.pack(side=tk.LEFT)

        # Button to create nested frame
        self.create_frame_button = tk.Button(self.main_frame, text="Add Item", command=self.ask_for_item_number)
        self.create_frame_button.grid(row=0, column=6, padx=10, pady=5, sticky=tk.E)

        # Create Empty frame to fill space
        self.invisible_frame = ctk.CTkFrame(self.main_frame, width=400, height=1)
        self.invisible_frame.grid(row=0, column=0, padx=1, pady=1)

        # Label to display total
        self.total_label = tk.Label(self.root, text="Total: $0.00")
        self.total_label.pack()

        # Dictionary to store prices of added items
        self.item_prices = {}

    def ask_for_item_number(self):
        item_number = simpledialog.askstring("Item Number", "Enter the item number:")
        if item_number and item_number.isdigit():
            self.create_nested_frame(item_number)
        else:
            messagebox.showerror("Error", "Please enter a valid item number.")

    def create_nested_frame(self, item_number):
        # Connect to the SQLite database
        receipts_db = sqlite3.connect('receipts.db')
        c = receipts_db.cursor()

        # Retrieve item_name and price from the database based on item_number
        c.execute("SELECT item_name, price FROM items_purchased WHERE item_id = ?", (item_number,))
        result = c.fetchone()

        # Close the database connection
        receipts_db.close()

        if result:
            item_name, price = result[0], result[1]
            self.item_prices[item_number] = price

            # Create a nested frame within the main frame
            nested_frame = ctk.CTkFrame(self.main_frame)
            nested_frame.grid(row=self.row_index, column=0, padx=20, pady=20)

            # Label to the left of the buttons using the retrieved item_name
            label = tk.Label(nested_frame, text=item_name)
            label.grid(row=0, column=0, columnspan=2, sticky=tk.W)

            # Label to the right inside the frame displaying the item price
            price_label = tk.Label(nested_frame, text=f"${price:.2f}")
            price_label.grid(row=0, column=2, columnspan=2, sticky=tk.E)

            # Create a button within the nested frame to remove the item
            remove_button = tk.Button(nested_frame, text="Remove Item", command=lambda: self.remove_nested_frame(nested_frame, item_number))
            remove_button.grid(row=1, column=0, padx=10, pady=5, columnspan=4)

            # Update total label
            self.update_total_label()

            # Increment the row index for the next frame
            self.row_index += 1
        else:
            messagebox.showwarning("Warning", f"Item with ID {item_number} not found")

    def remove_nested_frame(self, frame_to_remove, item_number):
        # Function to remove the specified nested frame
        frame_to_remove.destroy()

        # Remove item from the prices dictionary
        if item_number in self.item_prices:
            del self.item_prices[item_number]

        # Update total label
        self.update_total_label()

    def update_total_label(self):
        total = sum(self.item_prices.values())
        self.total_label.config(text=f"Total: ${total:.2f}")

    def on_button_click(self, item_number, action_number):
        print(f"Item {item_number}, Action {action_number} clicked")

# -----------------------------------

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

    root = ctk.CTk()
    ctk.set_appearance_mode("dark")

    app = left_side_scrl(root)
    root.mainloop()

if __name__ == "__main__":
    main()
