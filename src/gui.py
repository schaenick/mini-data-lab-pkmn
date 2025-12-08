import tkinter as tk
from data_loader import type_list, load_type, pokemon_df, type_advantages
from type_analysis import count_type_advantage, count_pokemon_of_type
from score_analysis import ranked_df
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def build_window():
    window = tk.Tk()
    window.geometry("600x600")
    window.title("Pokémon Type Analyzer")
    window.resizable(False, False)
    greeting = tk.Label(text="Choose your type: ")
    greeting.pack(pady=10)
    greeting.config(font=("Arial", 14, "bold"))

    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    info_frame = tk.Frame(window)
    info_frame.pack(pady=10, fill="x")

    plot_frame = tk.Frame(window, bg="#f0f0f0", height=300)
    plot_frame.pack(pady=5, fill="both", expand=True)

    def clear_plot():
        for widget in plot_frame.winfo_children():
            widget.destroy()

    def plot_type_detail_embed(
        type_name: str, stronger: int, weaker: int, equal: int, noeff: int
    ):
        clear_plot()

        categories = ["Stärker", "Schwächer", "Gleich", "Kein Effekt"]
        values = [stronger, weaker, equal, noeff]

        fig = Figure(figsize=(5, 3))
        ax = fig.add_subplot(111)
        ax.bar(categories, values)
        ax.set_title(f"Effektivitätsprofil für {type_name.title()}")
        ax.set_ylabel("Anzahl Pokémon")

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def plot_global_ranking_embed():
        clear_plot()

        df_sorted = ranked_df.sort_values("score", ascending=False)

        fig = Figure(figsize=(6, 3.5))
        ax = fig.add_subplot(111)
        ax.bar(df_sorted["type"], df_sorted["score"])
        ax.set_title("Globales Typ-Ranking (Score)")
        ax.set_xlabel("Typ")
        ax.set_ylabel("Score")
        ax.tick_params(axis="x", rotation=45)

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def button_click(poke_type, info_frame):
        stronger, weaker, equal, noeff = count_type_advantage(
            load_type(type_advantages), pokemon_df, poke_type
        )
        type_count = count_pokemon_of_type(pokemon_df, poke_type)

        row = ranked_df[ranked_df["type"] == poke_type].iloc[0]
        score = row["score"]
        rank = int(row["rank"])
        max_rank = len(ranked_df)

        for widget in info_frame.winfo_children():
            widget.destroy()

        header = tk.Label(
            info_frame,
            text=f"Typ: {poke_type.title()} – {type_count} Pokémon",
            font=("Arial", 12, "bold"),
            anchor="w",
            justify="left",
        )
        header.pack(anchor="w", padx=20)

        rank_label = tk.Label(
            info_frame,
            text=f"Rang: {rank} von {max_rank} – Score: {score}",
            anchor="w",
            justify="left",
        )
        rank_label.pack(anchor="w", padx=30, pady=(0, 5))

        label1 = tk.Label(
            info_frame,
            text=f"• Stärker als {stronger} Pokémon",
            anchor="w",
            justify="left",
        )
        label2 = tk.Label(
            info_frame,
            text=f"• Schwächer als {weaker} Pokémon",
            anchor="w",
            justify="left",
        )
        label3 = tk.Label(
            info_frame,
            text=f"• Genauso effektiv wie {equal} Pokémon",
            anchor="w",
            justify="left",
        )
        label4 = tk.Label(
            info_frame,
            text=f"• Kein Effekt gegen {noeff} Pokémon",
            anchor="w",
            justify="left",
        )

        label1.pack(anchor="w", padx=30)
        label2.pack(anchor="w", padx=30)
        label3.pack(anchor="w", padx=30)
        label4.pack(anchor="w", padx=30)
        plot_type_detail_embed(poke_type, stronger, weaker, equal, noeff)

    max_columns = 6
    row = 0
    col = 0

    for poke_type in type_list:
        btn = tk.Button(
            button_frame,
            text=poke_type.title(),
            width=10,
            command=lambda t=poke_type, m=info_frame: button_click(t, m),
        )

        btn.grid(row=row, column=col, padx=5, pady=5)

        col += 1
        if col >= max_columns:
            col = 0
            row += 1
    ranking_button = tk.Button(
        window,
        text="Globales Ranking anzeigen",
        command=plot_global_ranking_embed,
    )
    ranking_button.pack(pady=5)
    window.mainloop()


if __name__ == "__main__":
    build_window()
