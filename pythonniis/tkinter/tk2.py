import tkinter as tk

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")

# Entry box
entry = tk.Entry(root, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, pady=10)

# Buttons frame
frame = tk.Frame(root)
frame.pack()

# Button layout
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','C','=','+']
]

for row in buttons:
    for btn in row:
        if btn == "C":
            action = clear
        elif btn == "=":
            action = calculate
        else:
            action = lambda x=btn: click(x)

        tk.Button(frame, text=btn, width=5, height=2,
                  font=("Arial", 14),
                  command=action).pack(side="left", padx=5, pady=5)
    tk.Label(frame).pack()  # new line

root.mainloop()