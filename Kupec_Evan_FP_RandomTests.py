import tkinter as tk
from tkinter import scrolledtext
import random

def change_text():
    text = random.choice(["Hello!", "Welcome!", "Tkinter is fun!", "Python GUI", "Random Text"])
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Seamless Tkinter GUI")
root.geometry("400x300")
root.configure(bg="lightgrey")

# Create a frame with a darker grey background for the buttons
buttons_frame = tk.Frame(root, bg="darkgrey")
buttons_frame.pack(side=tk.RIGHT, fill=tk.Y)

# Create buttons with different text colors
button_colors = ["red", "green", "blue", "purple", "orange", "brown"]

for color in button_colors:
    button = tk.Button(buttons_frame, text=f"Button", fg=color, command=change_text)
    button.pack(side=tk.TOP, pady=5, padx=5)

# Create text box on the left side and make it fill the available space
text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=20, height=10, bg="white")
text_box.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)

# Run the main loop
root.mainloop()
