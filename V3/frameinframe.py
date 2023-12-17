import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Nested Frames Example")

        # Create the main frame
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.pack()

        # Entry for entering item number
        self.item_entry = tk.Entry(self.main_frame)
        self.item_entry.grid(row=0, column=0, padx=10, pady=5)

        # Button to create nested frame
        self.create_frame_button = tk.Button(self.main_frame, text="Create Frame", command=self.create_nested_frame)
        self.create_frame_button.grid(row=0, column=1, padx=10, pady=5)

    def create_nested_frame(self):
        item_number = self.item_entry.get()

        if item_number.isdigit():
            # Create a nested frame within the main frame
            nested_frame = tk.Frame(self.main_frame, bd=2, relief=tk.GROOVE)
            nested_frame.grid(row=int(item_number), column=0, padx=20, pady=20)

            # Label above the buttons
            label = tk.Label(nested_frame, text=f"Item {item_number}")
            label.grid(row=0, column=0, columnspan=3)

            # Create three buttons within the nested frame
            button1 = tk.Button(nested_frame, text="Action 1", command=lambda: self.on_button_click(item_number, 1))
            button1.grid(row=1, column=0, padx=10, pady=5)

            button2 = tk.Button(nested_frame, text="Action 2", command=lambda: self.on_button_click(item_number, 2))
            button2.grid(row=1, column=1, padx=10, pady=5)

            button3 = tk.Button(nested_frame, text="Action 3", command=lambda: self.on_button_click(item_number, 3))
            button3.grid(row=1, column=2, padx=10, pady=5)
        else:
            print("Please enter a valid item number.")

    def on_button_click(self, item_number, action_number):
        print(f"Item {item_number}, Action {action_number} clicked")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
