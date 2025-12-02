import pandas
from data_loader import load_data, load_type

# type = input("Choose a type!").lower().strip()
type = "fire"
pokemon_data_set = "data\\pokemon_data.csv"
type_advantages = "data\\type_advantage_data.csv"


def count_pokemon_of_type(df, type_name):
    mask = (df["type1"] == type_name) | (df["type2"] == type_name)
    return mask.sum()


def count_type_advantage(df, type_name):
    type_df = df[df["attacker"] == type_name]

    stronger = (type_df["effectiveness"] == 2).sum()
    equal = (type_df["effectiveness"] == 1).sum()
    weaker = (type_df["effectiveness"] == 0.5).sum()
    no_eff = (type_df["effectiveness"] == 0).sum()

    return stronger, weaker, equal, no_eff


stronger, weaker, equal, noeff = count_type_advantage(load_type(type_advantages), type)
type_count = count_pokemon_of_type(load_data(pokemon_data_set), type)
print(type_count, stronger, weaker, equal, noeff)
