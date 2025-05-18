import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Geometry & Colors Example")
root.geometry("400x250")
root.configure(bg="#2e2e2e")  # background in dark grey using HEX

# Frame using 'place'
frame = tk.Frame(root, bg="#004466", width=200, height=100)
frame.place(x=100, y=30)  # x and y coordinates

# Label using 'pack'
label = tk.Label(frame, text="Welcome!", fg="white", bg="#004466", font=("Arial", 14))
label.pack(pady=10)

# Entry and Button using 'grid'
entry = tk.Entry(root, width=20, bg="#ffffff", fg="#000000")
entry.grid(row=1, column=0, padx=10, pady=130)

def show_entry():
    user_input = entry.get()
    label.config(text=f"Hello, {user_input}!")

btn = tk.Button(root, text="Submit", bg="#33cc33", fg="white", command=show_entry)
btn.grid(row=1, column=1, padx=10, pady=130)

# Start the GUI loop
root.mainloop()
