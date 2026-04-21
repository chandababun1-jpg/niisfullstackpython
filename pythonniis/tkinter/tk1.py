import tkinter as tk

def add_numbers():
    try:
        n1 = int(entry1.get())
        n2 = int(entry2.get())
        n3 = int(entry3.get())
        result_label.config(text="Result: " + str(n1 + n2 + n3))
    except:
        result_label.config(text="Enter valid numbers!")

root = tk.Tk()
root.title("Add 3 Numbers")

tk.Label(root, text="Enter Number 1").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Number 2").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Enter Number 3").pack()
entry3 = tk.Entry(root)
entry3.pack()

tk.Button(root, text="Add", command=add_numbers).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()