import pandas as pd

def clean_games() -> pd.DataFrame:
    raw_games_data = pd.read_csv("games.csv")
    year_mask = (raw_games_data["season"] >= 2012) & (raw_games_data["season"] <= 2025)
    cleaned_games_data = raw_games_data[year_mask]
    return cleaned_games_data