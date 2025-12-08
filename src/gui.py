import tkinter as tk
from data_loader import type_list

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


def button_click(poke_type):
    print(poke_type)
    return


for poke_type in type_list:
    btn = tk.Button(
        button_frame,
        text=poke_type.title(),
        width=10,
        command=lambda t=poke_type: button_click(t),
    )

    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col >= max_columns:
        col = 0
        row += 1
window.mainloop()
