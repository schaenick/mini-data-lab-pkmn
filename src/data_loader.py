import pandas as pd


def load_data(data_set):
    pokemon_list = pd.read_csv(data_set, usecols=["name", "types"])
    types_split = pokemon_list["types"].str.split(",", n=1, expand=True)
    pokemon_list["type1"] = types_split[0].str.strip()
    pokemon_list["type2"] = types_split[1].str.strip()
    pokemon_list = pokemon_list.drop(columns=["types"])
    return pokemon_list


def load_type(type_data):
    type_adv_list = pd.read_csv(type_data)
    type_adv_list["attacker"] = type_adv_list["attacker"].str.strip().str.lower()
    type_adv_list["defender"] = type_adv_list["defender"].str.strip().str.lower()
    type_adv_list["effectiveness"] = type_adv_list["effectiveness"].astype(float)
    return type_adv_list


pokemon_data_set = "data\\pokemon_data.csv"
type_advantages = "data\\type_advantage_data.csv"
pokemon_df = load_data(pokemon_data_set)
type_list = pd.concat([pokemon_df["type1"], pokemon_df["type2"]]).dropna().unique()
