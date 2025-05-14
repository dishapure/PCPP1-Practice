from tkinter import *
from tkinter import messagebox

# create main window
root = Tk()
root.title("Simple GUI")
root.geometry("300x200")

# create label
label = Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.place(x=70, y=30)

# create frame
frame = Frame(root, bg="lightblue", width=280, height=50)
frame.place(x=10, y=70)

# event handler function
def on_click():
    messagebox.showinfo("Clicked", "You clicked the button!")
    root.destroy()

# create button
button = Button(root, text="Click Me", command=on_click)
button.place(x=110, y=80)

# start event loop
root.mainloop()
