import tkinter as tk

types = ["fire", "water", "grass", "rock", "bug", "ghost", "fairy"]

window = tk.Tk()
window.geometry("600x400")
window.title("Pokémon Type Analyzer")

greeting = tk.Label(text="Choose your type: ")
greeting.pack(pady=10)
greeting.pack()

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

max_columns = 3
row = 0
col = 0
for poke_type in types:
    btn = tk.Button(button_frame, text=poke_type, width=10)
    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col >= max_columns:
        col = 0
        row += 1
window.mainloop()
