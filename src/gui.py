# import tkinter as tk
import customtkinter as ctk
from type_analysis import count_type_advantage, count_pokemon_of_type
from score_analysis import ranked_df
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from initialization import type_list, pokemon_df, type_adv_df

from visualizations import create_type_detail_figure, create_global_ranking_figure


def build_window():
    window = ctk.CTk()

    window.title("Pokémon Type Analyzer")
    window.resizable(False, False)
    greeting = ctk.CTkLabel(
        master=window,
        text="Wähle einen Typ oder das globale Ranking:",
        font=ctk.CTkFont(size=16, weight="bold"),
    )
    greeting.pack(pady=(20, 10))

    button_frame = ctk.CTkFrame(window)
    button_frame.pack(pady=5, padx=10, fill="x")

    info_frame = ctk.CTkFrame(window)
    info_frame.pack(pady=10, padx=10, fill="x")

    plot_frame = ctk.CTkFrame(window, height=350)
    plot_frame.pack(pady=5, padx=10, fill="both", expand=True)

    ranking_button_frame = ctk.CTkFrame(window)
    ranking_button_frame.pack(pady=(0, 10), fill="x")

    def clear_plot():
        for widget in plot_frame.winfo_children():
            widget.destroy()

    def plot_type_detail_embed(
        type_name: str, stronger: int, weaker: int, equal: int, noeff: int
    ):
        clear_plot()

        fig = create_type_detail_figure(type_name, stronger, weaker, equal, noeff)

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def plot_global_ranking_embed():
        clear_plot()

        fig = create_global_ranking_figure(ranked_df)

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def button_click(poke_type, info_frame):
        stronger, weaker, equal, noeff = count_type_advantage(
            type_adv_df, pokemon_df, poke_type
        )
        type_count = count_pokemon_of_type(pokemon_df, poke_type)

        row = ranked_df[ranked_df["type"] == poke_type].iloc[0]
        score = row["score"]
        rank = int(row["rank"])
        max_rank = len(ranked_df)

        for widget in info_frame.winfo_children():
            widget.destroy()

        header = ctk.CTkLabel(
            info_frame,
            text=f"{poke_type.title()} Typ-Analyse",
            font=ctk.CTkFont(size=18, weight="bold"),
            anchor="center",
        )
        header.pack(pady=(15, 5))

        summary_text = (
            f"Pokémon: {type_count}   |   "
            f"Rang: {rank} von {max_rank}   |   "
            f"Score: {score}"
        )
        summary_label = ctk.CTkLabel(
            info_frame,
            text=summary_text,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#1F6AA5",
        )
        summary_label.pack(pady=(5, 15))

        separator = ctk.CTkFrame(info_frame, height=2, fg_color="gray", border_width=0)
        separator.pack(fill="x", padx=20)

        detail_header = ctk.CTkLabel(
            info_frame,
            text="Effektivität gegenüber anderen Pokémon:",
            font=ctk.CTkFont(size=13, weight="bold"),
            anchor="w",
        )
        detail_header.pack(anchor="w", padx=20, pady=(15, 5))

        row1_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
        row1_frame.pack(fill="x", padx=30, pady=2)

        label1 = ctk.CTkLabel(
            row1_frame,
            text=f"⬆️ Stärker als {stronger} Pokémon",
            anchor="w",
            width=250,
        )
        label2 = ctk.CTkLabel(
            row1_frame, text=f"⬇️ Schwächer als {weaker} Pokémon", anchor="w", width=250
        )

        label1.pack(side="left", padx=10, expand=True)
        label2.pack(side="right", padx=10, expand=True)

        row2_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
        row2_frame.pack(fill="x", padx=30, pady=(2, 15))

        label3 = ctk.CTkLabel(
            row2_frame,
            text=f"🤝 Genauso effektiv wie {equal} Pokémon",
            anchor="w",
            width=250,
        )
        label4 = ctk.CTkLabel(
            row2_frame,
            text=f"🛡️ Kein Effekt gegen {noeff} Pokémon",
            anchor="w",
            width=250,
        )

        label3.pack(side="left", padx=10, expand=True)
        label4.pack(side="right", padx=10, expand=True)

        plot_type_detail_embed(poke_type, stronger, weaker, equal, noeff)

    max_columns = 6
    row = 0
    col = 0

    for poke_type in type_list:

        btn = ctk.CTkButton(
            button_frame,
            text=poke_type.title(),
            width=100,
            command=lambda t=poke_type, m=info_frame: button_click(t, m),
            corner_radius=8,
        )

        btn.grid(row=row, column=col, padx=5, pady=5)

        col += 1
        if col >= max_columns:
            col = 0
            row += 1

    ranking_button = ctk.CTkButton(
        ranking_button_frame,
        text="Globales Ranking anzeigen",
        command=plot_global_ranking_embed,
        font=ctk.CTkFont(size=12, weight="bold"),
    )
    ranking_button.pack(pady=5)

    plot_global_ranking_embed()
    window.update()
    window.minsize(window.winfo_width(), window.winfo_height())
    window.mainloop()


if __name__ == "__main__":
    build_window()
