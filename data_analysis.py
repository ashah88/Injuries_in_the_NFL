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
    merged = pd.read_csv("games_and_injuries.csv")
    injuries = pd.read_csv("cleaned_injuries.csv")
    shape_merged = merged.shape
    shape_injuries = injuries.shape
    print(f"(Rows,Columns) Merged:{shape_merged}. Injuries:{shape_injuries}")

    num_missing_merged = merged.isna().sum()
    print(f"NA entries in games_and_injuries.csv: {num_missing_merged}")
    num_missing_injuries = injuries.isna().sum()
    print(f"Num NA entires in cleaned_injuries.csv: {num_missing_injuries}")
    print(f"Injuries described: {injuries.describe()}")
    print(f"Merged described: {merged.describe()}")
    print(f"Position counts: {injuries["position"].value_counts()}")
    print(f"Status counts: {injuries["report_status"].value_counts()}")
    print(f"Teams in merged: {merged["team"].value_counts()}")
    print(f"Teams in injuries: {injuries["team"].value_counts()}")
    print(f"Number of game ids: {merged["game_id"].nunique()}")


if __name__ == '__main__':
    main()
