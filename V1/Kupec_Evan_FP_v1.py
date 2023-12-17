import customtkinter as ctk

window = ctk.CTk()
ctk.set_appearance_mode("dark")
window.title('customtkinter app')
window.geometry('600x400')

#-------------------------

def button_test():
    print("button pressed")

#-------------------------

frame = ctk.CTkFrame(window, width=200, height=200, border_width=2, border_color='green')
frame.grid(column=0, row=0, columnspan=4, rowspan=5, padx=4, pady=2)

button1 = ctk.CTkButton(window, text="Hello1", command=button_test)
button1.grid(column=5, row=0)
button2 = ctk.CTkButton(window, text="Hello2", command=button_test)
button2.grid(column=5, row=1)
button3 = ctk.CTkButton(window, text="Hello3", command=button_test)
button3.grid(column=5, row=2)
button4 = ctk.CTkButton(window, text="Hello4", command=button_test)
button4.grid(column=5, row=3)
button5 = ctk.CTkButton(window, text="Hello5", command=button_test)
button5.grid(column=5, row=4)

#-------------------------

window.mainloop()