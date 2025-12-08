def count_pokemon_of_type(df, type_name):
    """
    Counts all Pokémon that possess the given type (as either Type 1 or Type 2).

    Args:
        df (pd.DataFrame): The Pokémon DataFrame.
        type_name (str): The Pokémon type being searched for.

    Returns:
        int: The number of Pokémon of this type.
    """
    # Creates a boolean mask for Type 1 OR Type 2 matching the type_name
    mask = (df["type1"] == type_name) | (df["type2"] == type_name)
    return mask.sum()


def count_type_advantage(type_advantages, pokemon_data_set, type_name):
    """
    Calculates how many Pokémon are hit harder, weaker, neutrally, or immune
    by the selected attacker type.

    Args:
        type_adv_df (pd.DataFrame): The type advantage DataFrame.
        pokemon_df (pd.DataFrame): The DataFrame of all Pokémon.
        type_name (str): The attacking type.

    Returns:
        tuple: (stronger_pokemon, weaker_pokemon, equal_pokemon, no_eff_pokemon)
    """
    # Filters the rows relevant to the current attacking type
    type_df = type_advantages[type_advantages["attacker"] == type_name]

    # Extracts lists of defender types based on effectiveness (2, 1, 0.5, 0)
    stronger = type_df.loc[type_df["effectiveness"] == 2, "defender"].tolist()
    equal = type_df.loc[type_df["effectiveness"] == 1, "defender"].tolist()
    weaker = type_df.loc[type_df["effectiveness"] == 0.5, "defender"].tolist()
    no_eff = type_df.loc[type_df["effectiveness"] == 0, "defender"].tolist()

    # Count Pokémon whose Type 1 OR Type 2 is in the respective defender lists

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
