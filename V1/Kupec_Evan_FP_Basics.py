import tkinter as tk
root = tk.Tk()

#--->This was from a video i followed where he started...
#--->...to make a calculator as he explained the basics

root.geometry("500x500")
root.title("My First tkinter")

label = tk.Label(root, text="Howdy Yall", font=('Arial', 18))
label.pack(padx=2, pady=2)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack()

#myentry = tk.Entry(root)
#myentry.pack()

#button = tk.Button(root, text="Click this", font=('Arial', 10))
#button.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

root.mainloop()