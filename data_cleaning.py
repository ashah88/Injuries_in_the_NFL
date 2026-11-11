"""
Jack Kjar
CSE 163 AE
This file contains a script that cleans our injuries and game datasets.
It merges all injuries datasets into one master set, and keeps only the
columns we need for our research questions in the games and master injury
datasets.
"""

import pandas as pd


def clean_games() -> pd.DataFrame:
    """
    Returns a pandas dataframe of the "games.csv" file containing only games
    between 2012 and 2015, and only the columns needed for our project.
    """
    raw_games_data = pd.read_csv("games.csv")
    lower_year_mask = raw_games_data["season"] >= 2012
    upper_year_mask = raw_games_data["season"] <= 2025
    cleaned_games_data = raw_games_data[lower_year_mask & upper_year_mask]
    games_master = cleaned_games_data[["game_id", "season", "week",
                                       "home_team", "away_team",
                                       "home_rest", "away_rest"]].copy()
    teams = ["home_team", "away_team"]
    filter = {"SD": "LAC", "STL": "LA", "OAK": "LV"}
    games_master[teams] = games_master[teams].replace(filter)
    return games_master


def clean_injuries() -> pd.DataFrame:
    """
    Returns a Pandas dataframe of all "injuries_<year>.csv" files merged into
    one, containing only the columns needed for our project. Also updates all
    team designators to their current day values.
    """
    injuries_2012 = pd.read_csv("injuries_2012.csv")
    injuries_2013 = pd.read_csv("injuries_2013.csv")
    injuries_2014 = pd.read_csv("injuries_2014.csv")
    injuries_2015 = pd.read_csv("injuries_2015.csv")
    injuries_2015 = pd.read_csv("injuries_2015.csv")
    injuries_2016 = pd.read_csv("injuries_2016.csv")
    injuries_2017 = pd.read_csv("injuries_2017.csv")
    injuries_2018 = pd.read_csv("injuries_2018.csv")
    injuries_2019 = pd.read_csv("injuries_2019.csv")
    injuries_2020 = pd.read_csv("injuries_2020.csv")
    injuries_2021 = pd.read_csv("injuries_2021.csv")
    injuries_2022 = pd.read_csv("injuries_2022.csv")
    injuries_2023 = pd.read_csv("injuries_2023.csv")
    injuries_2024 = pd.read_csv("injuries_2024.csv")
    injuries_2025 = pd.read_csv("injuries_2025.csv")
    cleaned_injuries = pd.concat([injuries_2012, injuries_2013, injuries_2014,
                                  injuries_2015, injuries_2016, injuries_2017,
                                  injuries_2018, injuries_2019, injuries_2020,
                                  injuries_2021, injuries_2022, injuries_2023,
                                  injuries_2024, injuries_2025],
                                 ignore_index=True)
    injuries_master = cleaned_injuries[["season", "team", "week", "position",
                                        "report_status"]].copy()
    filter = {"SD": "LAC", "STL": "LA", "OAK": "LV"}
    injuries_master["team"] = injuries_master["team"].replace(filter)
    return injuries_master


def main():
    games_data = clean_games()
    injuries_data = clean_injuries()
    games_data.to_csv("cleaned_games.csv")
    injuries_data.to_csv("cleaned_injuries.csv")


if __name__ == "__main__":
    main()
