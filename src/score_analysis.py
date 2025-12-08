from type_analysis import count_type_advantage, count_pokemon_of_type
from initialization import type_list, pokemon_df
import pandas as pd
from initialization import type_list, pokemon_df, type_adv_df

WEIGHT_STRONGER = 2.0
WEIGHT_EQUAL = 1.0
WEIGHT_WEAKER = -1.0
WEIGHT_NO_EFF = -2.0


ranked = []
for entry in type_list:
    stronger, weaker, equal, noeff = count_type_advantage(
        type_adv_df, pokemon_df, entry
    )
    type_count = count_pokemon_of_type(pokemon_df, entry)
    score = (
        (stronger * WEIGHT_STRONGER)
        + (equal * WEIGHT_EQUAL)
        + (weaker * WEIGHT_WEAKER)
        + (noeff * WEIGHT_NO_EFF)
    )
    ranked.append(
        {
            "type": entry,
            "score": score,
            "num_pokemon": int(type_count),
        }
    )
ranked_df = pd.DataFrame(ranked)
ranked_df = ranked_df.sort_values("score", ascending=False).reset_index(drop=True)
ranked_df["rank"] = ranked_df.index + 1
