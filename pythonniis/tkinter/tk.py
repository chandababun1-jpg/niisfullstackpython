import tkinter as tk

def add_numbers():
    n1 = int(entry1.get())
    n2 = int(entry2.get())
    result = n1 + n2
    label_result.config(text="Result: " + str(result))

# Create window
root = tk.Tk()
root.title("Add 2 Numbers")
root.geometry("300x200")

# Input fields
entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Button
btn = tk.Button(root, text="Add", command=add_numbers)
btn.pack()

# Result label
label_result = tk.Label(root, text="Result: ")
label_result.pack()

# Run app
root.mainloop()