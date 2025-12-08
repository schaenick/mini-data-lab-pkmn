from type_analysis import count_type_advantage, count_pokemon_of_type
from initialization import type_list, pokemon_df
import pandas as pd
from initialization import type_list, pokemon_df, type_adv_df

# --- WEIGHTED SCORING SYSTEM (Offensive Dominance) ---
# Weights for calculating the final score of a type based on user request.
# High reward for dominance (x2) and high penalty for uselessness (x-2).

WEIGHT_STRONGER = 2.0
WEIGHT_EQUAL = 1.0
WEIGHT_WEAKER = -1.0
WEIGHT_NO_EFF = -2.0


ranked = []
for entry in type_list:
    # Retrieve the counts for the current type
    stronger, weaker, equal, noeff = count_type_advantage(
        type_adv_df, pokemon_df, entry
    )
    type_count = count_pokemon_of_type(pokemon_df, entry)
    # Calculate the weighted score
    score = (
        (stronger * WEIGHT_STRONGER)
        + (equal * WEIGHT_EQUAL)
        + (weaker * WEIGHT_WEAKER)
        + (noeff * WEIGHT_NO_EFF)
    )
    # Store results in the ranking array
    ranked.append(
        {
            "type": entry,
            "score": score,
            "num_pokemon": int(type_count),
        }
    )
# Create the final DataFrame
ranked_df = pd.DataFrame(ranked)

# Sort the DataFrame by score descending
ranked_df = ranked_df.sort_values("score", ascending=False).reset_index(drop=True)

# Add the final rank column (Index + 1)
ranked_df["rank"] = ranked_df.index + 1
