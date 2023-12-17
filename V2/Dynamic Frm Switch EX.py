import tkinter as tk
from tkinter import ttk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Frame Switching")

        # Create a StringVar to store the selected option
        self.selected_option = tk.StringVar()

        # Create a frame for holding buttons
        button_frame = ttk.Frame(root, padding="10")
        button_frame.grid(row=0, column=0)

        # Create buttons to switch frames
        button1 = ttk.Button(button_frame, text="Frame 1", command=lambda: self.show_frame(Frame1))
        button1.grid(row=0, column=0, pady=5)

        button2 = ttk.Button(button_frame, text="Frame 2", command=lambda: self.show_frame(Frame2))
        button2.grid(row=1, column=0, pady=5)

        # Create the initial frame
        self.current_frame = None
        self.show_frame(Frame1)

    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.grid_forget()

        self.current_frame = frame_class(self.root, self.selected_option)
        self.current_frame.grid(row=0, column=1, padx=10, pady=10)

class Frame1(ttk.Frame):
    def __init__(self, master, selected_option):
        super().__init__(master)
        self.selected_option = selected_option

        # Frame-specific content
        label = ttk.Label(self, text="This is Frame 1")
        label.grid(row=0, column=0)

        # Entry to get user input
        entry = ttk.Entry(self, textvariable=self.selected_option)
        entry.grid(row=1, column=0, pady=5)

class Frame2(ttk.Frame):
    def __init__(self, master, selected_option):
        super().__init__(master)
        self.selected_option = selected_option

        # Frame-specific content
        label = ttk.Label(self, text="This is Frame 2")
        label.grid(row=0, column=0)

        # Dropdown menu to select options
        options = ["Option 1", "Option 2", "Option 3"]
        dropdown = ttk.Combobox(self, values=options, textvariable=self.selected_option)
        dropdown.grid(row=1, column=0, pady=5)

# Create the main application window
root = tk.Tk()
app = MyApp(root)
root.mainloop()
