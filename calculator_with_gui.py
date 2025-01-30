import tkinter as tk
import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect("calculator_history.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        operation TEXT,
        result TEXT
    )
""")
conn.commit()

def calculate(operation):
    try:
        result = eval(operation)
        display_var.set(result)
        
        # Save the operation to the database
        cursor.execute("INSERT INTO history (operation, result) VALUES (?, ?)", (operation, str(result)))
        conn.commit()
    except Exception as e:
        display_var.set("Error")

def show_history():
    cursor.execute("SELECT * FROM history")
    history = cursor.fetchall()
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    for entry in history:
        tk.Label(history_window, text=f"{entry[1]} = {entry[2]}").pack()

# GUI Setup
root = tk.Tk()
root.title("Basic Calculator")

display_var = tk.StringVar()

display = tk.Entry(root, textvariable=display_var, font=("Arial", 18), bd=10, insertwidth=4, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row_val, col_val = 1, 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18),
                  command=lambda: calculate(display_var.get())).grid(row=row_val, column=col_val)
    elif button == "C":
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18),
                  command=lambda: display_var.set("")).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18),
                  command=lambda b=button: display_var.set(display_var.get() + b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# History Button
tk.Button(root, text="History", padx=20, pady=20, font=("Arial", 18), command=show_history).grid(row=row_val, column=0, columnspan=4)

root.mainloop()
conn.close()
