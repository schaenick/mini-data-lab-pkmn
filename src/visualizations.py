import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def create_type_detail_figure(
    type_name: str, stronger: int, weaker: int, equal: int, no_eff: int
) -> Figure:
    categories = ["Stärker", "Schwächer", "Gleich", "Kein Effekt"]
    values = [stronger, weaker, equal, no_eff]

    fig = Figure(figsize=(5, 3))
    ax = fig.add_subplot(111)

    ax.bar(categories, values)

    ax.set_title(f"Effektivitätsprofil für {type_name.title()}")
    ax.set_ylabel("Anzahl Pokémon")

    fig.tight_layout()
    return fig


def create_global_ranking_figure(df) -> Figure:

    df_sorted = df.sort_values("score", ascending=False)

    fig = Figure(figsize=(6, 3.5))
    ax = fig.add_subplot(111)

    ax.bar(df_sorted["type"], df_sorted["score"])

    ax.set_title("Globales Typ-Ranking (Score)")
    ax.set_xlabel("Typ")
    ax.set_ylabel("Score")
    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    return fig
