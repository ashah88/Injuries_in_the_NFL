"""
Jack Kjar
CSE 163 AE
This file contains a script that finds the shape/size of our datasets, and
the number of missing entries in our datasets.
"""
import pandas as pd


def main() -> None:
    """
    Finds and prints the shape of each dataset and the number of missing
    entries in each dataset.
    """
    games = pd.read_csv("cleaned_games.csv")
    injuries = pd.read_csv("cleaned_injuries.csv")
    shape_games = games.shape
    shape_injuries = injuries.shape
    print(f"(Rows, Columns) Games: {shape_games}. Injuries: {shape_injuries}")

    num_missing_games = games.isna().sum()
    print(f"Amount of NA entries in cleaned_games.csv: {num_missing_games}")
    num_missing_injuries = injuries.isna().sum()
    print(f"Num NA entires in cleaned_injuries.csv: {num_missing_injuries}")


if __name__ == '__main__':
    main()
