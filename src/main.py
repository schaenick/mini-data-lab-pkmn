from type_analysis import count_type_advantage, count_pokemon_of_type
from data_loader import load_data, load_type


# type = input("Choose a type!").lower().strip()
type = "rock"
pokemon_data_set = "data\\pokemon_data.csv"
type_advantages = "data\\type_advantage_data.csv"

pokemon_df = load_data(pokemon_data_set)


stronger, weaker, equal, noeff = count_type_advantage(
    load_type(type_advantages), pokemon_df, type
)
type_count = count_pokemon_of_type(pokemon_df, type)
print(type_count, stronger, weaker, equal, noeff)
