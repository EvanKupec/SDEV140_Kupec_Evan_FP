import customtkinter as ctk
import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3

class LeftSideScrl:
    def __init__(self, root):
        self.root = root
        self.root.title('Guest Service: Returns')
        # self.root.geometry('600x400')

        # Create the main frame
        self.main_frame = ctk.CTkScrollableFrame(self.root)
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

        # Create a frame for buttons and total label
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # Button to create nested frame
        self.create_frame_button = tk.Button(self.button_frame, text="Add Item", command=self.ask_for_item_number)
        self.create_frame_button.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        # Button to create nested frame
        self.adjust_price_button = tk.Button(self.button_frame, text="Wrong Price", command=self.adjust_price_popup)
        self.adjust_price_button.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        # Label to display total
        self.total_label = tk.Label(self.button_frame, text="Total: $0.00", justify=tk.CENTER)
        self.total_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        # Button to create refund pop-up
        self.refund_button = tk.Button(self.button_frame, text="Refund", command=self.refund_popup, state=tk.DISABLED)
        self.refund_button.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

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
            nested_frame.grid(row=len(self.item_prices), column=0, padx=20, pady=20)

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

        # Enable or disable the refund button based on the total amount
        if total > 0:
            self.refund_button.config(state=tk.NORMAL)
        else:
            self.refund_button.config(state=tk.DISABLED)

    def adjust_price_popup(self):
        item_id = simpledialog.askstring("Item ID", "Enter the item ID for price adjustment:")
        if item_id and item_id.isdigit():
            # Connect to the SQLite database
            receipts_db = sqlite3.connect('receipts.db')
            c = receipts_db.cursor()

            # Retrieve the item_name and current price from the database based on item_id
            c.execute("SELECT item_name, price FROM items_purchased WHERE item_id = ?", (item_id,))
            result = c.fetchone()

            # Close the database connection
            receipts_db.close()

            if result:
                item_name, current_price = result[0], result[1]
                new_price = simpledialog.askfloat("Wrong Price", f"Item: {item_name}\nCurrent Price: ${current_price:.2f}\nWhat should be the new price?")

                if new_price is not None:
                    price_difference = current_price - new_price

                    if price_difference > 0:
                        messagebox.showinfo("Price Adjustment", f"Price Adjustment: ${price_difference:.2f} Refunded")
                    else:
                        messagebox.showinfo("Price Adjustment", "No refund necessary.")
            else:
                messagebox.showwarning("Warning", f"Item with ID {item_id} not found")

    def refund_popup(self):
        total = sum(self.item_prices.values())
        # Remove all nested frames
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.item_prices = {}  # Clear the item_prices dictionary
        self.total_label.config(text="Total: $0.00")  # Reset the total label
        self.refund_button.config(state=tk.DISABLED)  # Disable the refund button
        messagebox.showinfo("Refund Complete", f"Return Complete: ${total:.2f} Refunded")

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

    app = LeftSideScrl(root)
    root.mainloop()

if __name__ == "__main__":
    main()
