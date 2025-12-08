from type_analysis import count_type_advantage, count_pokemon_of_type
from data_loader import load_type, load_type, type_list, pokemon_df, type_advantages
import pandas as pd


# type = input("Choose a type!").lower().strip()


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
