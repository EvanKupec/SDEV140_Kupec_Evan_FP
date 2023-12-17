import sqlite3
from datetime import date

# Connect to the SQLite database (or create it if it doesn't exist)
receipts_db = sqlite3.connect('receipts.db')

# Create a cursor object to execute SQL commands
c = receipts_db.cursor()

# Insert sample data into the receipts table
c.execute('''
    INSERT INTO receipts (receipt_number, purchase_date, customer_name)
    VALUES (?, ?, ?)
''', (1, date.today(), 'John Doe'))

# Insert sample data into the items_purchased table
c.execute('''
    INSERT INTO items_purchased (receipt_number, item_id, item_name, price)
    VALUES (?, ?, ?, ?)
''', (1, '123456789', 'Item1', 10.99))

c.execute('''
    INSERT INTO items_purchased (receipt_number, item_id, item_name, price)
    VALUES (?, ?, ?, ?)
''', (1, '987654321', 'Item2', 5.99))

# Commit the changes and close the connection
receipts_db.commit()
receipts_db.close()

print("Sample data with DPCI inserted successfully.")
