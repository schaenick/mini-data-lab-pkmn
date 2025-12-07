import matplotlib.pyplot as plt
from score_analysis import ranked_df


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


plot_type_scores(ranked_df)
