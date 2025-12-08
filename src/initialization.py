import pandas as pd
from data_loader import load_data, load_type

POKEMON_DATA_SET_PATH = "data\\pokemon_data.csv"
TYPE_ADVANTAGES_PATH = "data\\type_advantage_data.csv"

pokemon_df = load_data(POKEMON_DATA_SET_PATH)
type_adv_df = load_type(TYPE_ADVANTAGES_PATH)

type_list = pd.concat([pokemon_df["type1"], pokemon_df["type2"]]).dropna().unique()
