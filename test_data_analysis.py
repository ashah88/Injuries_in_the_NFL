"""
Jack Kjar
CSE 163 AE
This file contains a script that finds the shape/size of our datasets, the
number of missing entries in our datasets, the seven number summary of
each quantitative variable, and the counts of each categorical variable.
"""
import pandas as pd


def main() -> None:
    """
    Finds and prints the shape of each dataset. the number of missing
    entries in each dataset, the seven number summary of each quantitative
    variable, and the counts of each categorical variable.
    """
    games = pd.read_csv("test_games.csv")
    injuries = pd.read_csv("test_injuries.csv")
    shape_games = games.shape
    shape_injuries = injuries.shape
    print(f"(Rows, Columns) Games: {shape_games}. Injuries: {shape_injuries}")

    num_missing_games = games.isna().sum()
    print(f"Amount of NA entries in cleaned_games.csv: {num_missing_games}")
    num_missing_injuries = injuries.isna().sum()
    print(f"Num NA entires in cleaned_injuries.csv: {num_missing_injuries}")
    print(f"Injuries described: {injuries.describe()}")
    print(f"Games described: {games.describe()}")
    print(f"Position counts: {injuries["position"].value_counts()}")
    print(f"Status counts: {injuries["report_status"].value_counts()}")
    print(f"Home teams in games: {games["home_team"].value_counts()}")
    print(f"Away teams in games: {games["away_team"].value_counts()}")
    print(f"Teams in injuries: {injuries["team"].value_counts()}")


if __name__ == '__main__':
    main()
