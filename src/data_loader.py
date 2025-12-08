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
