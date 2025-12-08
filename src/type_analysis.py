import pandas as pd


def count_pokemon_of_type(df, type_name):
    mask = (df["type1"] == type_name) | (df["type2"] == type_name)
    return mask.sum()


def count_type_advantage(type_advantages, pokemon_data_set, type_name):
    type_df = type_advantages[type_advantages["attacker"] == type_name]
    stronger = type_df.loc[type_df["effectiveness"] == 2, "defender"].tolist()
    equal = type_df.loc[type_df["effectiveness"] == 1, "defender"].tolist()
    weaker = type_df.loc[type_df["effectiveness"] == 0.5, "defender"].tolist()
    no_eff = type_df.loc[type_df["effectiveness"] == 0, "defender"].tolist()

    stronger_mask = pokemon_data_set["type1"].isin(stronger) | pokemon_data_set[
        "type2"
    ].isin(stronger)
    stronger_pokemon = stronger_mask.sum()
    weaker_mask = pokemon_data_set["type1"].isin(weaker) | pokemon_data_set[
        "type2"
    ].isin(weaker)
    weaker_pokemon = weaker_mask.sum()

    equal_mask = pokemon_data_set["type1"].isin(equal) | pokemon_data_set["type2"].isin(
        equal
    )
    equal_pokemon = equal_mask.sum()

    no_eff_mask = pokemon_data_set["type1"].isin(no_eff) | pokemon_data_set[
        "type2"
    ].isin(no_eff)
    no_eff_pokemon = no_eff_mask.sum()

    return stronger_pokemon, weaker_pokemon, equal_pokemon, no_eff_pokemon
