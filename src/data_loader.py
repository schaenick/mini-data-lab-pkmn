import pandas as pd


def load_data(data_set):
    """
    Loads Pokémon data from the CSV, extracting and splitting types into two columns.

    Args:
        data_set_path (str): Path to the Pokémon data file.

    Returns:
        pd.DataFrame: DataFrame with 'name', 'type1', and 'type2' columns.
    """
    # Load only the required columns: name and types
    pokemon_list = pd.read_csv(data_set, usecols=["name", "types"])

    # Split the 'types' column by comma to isolate the two types
    types_split = pokemon_list["types"].str.split(",", n=1, expand=True)

    # Assign the split and cleaned (lowercase, stripped) types
    pokemon_list["type1"] = types_split[0].str.strip()
    # Ensure the second type is also cleaned
    pokemon_list["type2"] = types_split[1].str.strip()

    # Drop the original 'types' column
    pokemon_list = pokemon_list.drop(columns=["types"])
    return pokemon_list


def load_type(type_data):
    """
    Loads type advantage data and formats attacker/defender columns.

    Args:
        type_data_path (str): Path to the type advantage data file.

    Returns:
        pd.DataFrame: DataFrame with 'attacker', 'defender', 'effectiveness'.
    """

    type_adv_list = pd.read_csv(type_data)

    # Clean and standardize 'attacker' and 'defender' columns to lowercase
    type_adv_list["attacker"] = type_adv_list["attacker"].str.strip().str.lower()
    type_adv_list["defender"] = type_adv_list["defender"].str.strip().str.lower()

    # Ensure 'effectiveness' is a float
    type_adv_list["effectiveness"] = type_adv_list["effectiveness"].astype(float)
    return type_adv_list
