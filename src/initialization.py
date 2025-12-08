import pandas as pd
from data_loader import load_data, load_type

# --- DATA PATH DEFINITIONS ---
POKEMON_DATA_SET_PATH = "data\\pokemon_data.csv"
TYPE_ADVANTAGES_PATH = "data\\type_advantage_data.csv"

# --- DATA LOADING AND INITIALIZATION ---
# These variables are loaded once when the module is imported and are globally accessible
pokemon_df = load_data(POKEMON_DATA_SET_PATH)
type_adv_df = load_type(TYPE_ADVANTAGES_PATH)

# --- CREATE TYPE LIST ---
type_list = pd.concat([pokemon_df["type1"], pokemon_df["type2"]]).dropna().unique()
