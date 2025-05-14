from tkinter import *
from tkinter import messagebox

# Function to validate and show message
def submit():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()

    if not name:
        messagebox.showerror("Input Error", "Name cannot be empty!")
        return
    if not age.isdigit():
        messagebox.showerror("Input Error", "Age must be a number!")
        return

    canvas.create_text(150, 20, text=f"Hello {name} ({gender}), Age {age}", fill="blue", font=("Arial", 12))

# Function for key press binding
def on_key_press(event):
    messagebox.showinfo("Key Pressed", f"You pressed: {event.char}")

# Main window
root = Tk()
root.title("User Info App")
root.geometry("400x300")
root.bind("<Key>", on_key_press)  # bind key press event

# Name label and entry using grid
Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Age label and entry using grid
Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
age_entry = Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

# Gender Radiobuttons using place
gender_var = StringVar(value="Male")
Label(root, text="Gender:").place(x=30, y=70)
Radiobutton(root, text="Male", variable=gender_var, value="Male").place(x=100, y=70)
Radiobutton(root, text="Female", variable=gender_var, value="Female").place(x=160, y=70)

# Submit button
Button(root, text="Submit", command=submit).place(x=150, y=110)

# Canvas to draw text
canvas = Canvas(root, width=350, height=100, bg="lightyellow")
canvas.place(x=25, y=150)

root.mainloop()
