from type_analysis import count_type_advantage, count_pokemon_of_type
from data_loader import load_data, load_type
import pandas as pd


# type = input("Choose a type!").lower().strip()
pokemon_data_set = "data\\pokemon_data.csv"
type_advantages = "data\\type_advantage_data.csv"
pokemon_df = load_data(pokemon_data_set)

type_list = pd.concat([pokemon_df["type1"], pokemon_df["type2"]]).dropna().unique()

ranked = []
for entry in type_list:
    stronger, weaker, equal, noeff = count_type_advantage(
        load_type(type_advantages), pokemon_df, entry
    )
    type_count = count_pokemon_of_type(pokemon_df, entry)
    ranked.append(
        {
            "type": entry,
            "score": int(weaker) - int(stronger),
            "num_pokemon": int(type_count),
        }
    )
ranked_df = pd.DataFrame(ranked)
ranked_df = ranked_df.sort_values("score", ascending=False).reset_index(drop=True)
ranked_df["rank"] = ranked_df.index + 1
