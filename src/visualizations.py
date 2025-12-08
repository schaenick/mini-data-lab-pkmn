import matplotlib.pyplot as plt


def plot_type_scores(df):
    df_sorted = df.sort_values("score", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(df_sorted["type"], df_sorted["score"])
    plt.xticks(rotation=45)
    plt.xlabel("Pokémon Type")
    plt.ylabel("Score")
    plt.title("Pokémon Type Score Ranking")
    plt.tight_layout()
    plt.show()


def plot_type_detail(
    type_name: str, stronger: int, weaker: int, equal: int, no_eff: int
):
    categories = ["Stärker", "Schwächer", "Gleich effektiv", "Kein Effekt"]
    values = [stronger, weaker, equal, no_eff]

    plt.figure(figsize=(6, 4))
    plt.bar(categories, values)
    plt.title(f"Effektivitätsprofil für {type_name.title()}")
    plt.ylabel("Anzahl Pokémon")
    plt.tight_layout()
    plt.show()
