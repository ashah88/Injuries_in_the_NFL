"""
Name: Shreyas Sao
Section: <your section>

Find the NFL positions with the highest and lowest injury rates.
"""

import pandas as pd


def main() -> None:
    """
    Prints the number of reported injuries for each position, sorted
    from most to fewest, followed by the positions with the most and
    fewest. A player is counted once per season and week.
    """
    injuries = pd.read_csv("cleaned_injuries.csv")

    has_position = injuries["position"].str.strip() != ""
    valid = injuries[has_position]

    unique = valid.drop_duplicates(
        subset=["gsis_id", "season", "week"]
    )
    counts = unique["position"].value_counts()

    print(counts)
    print(f"\nMost injuries: {counts.index[0]} ({counts.iloc[0]})")
    print(f"Fewest injuries: {counts.index[-1]} ({counts.iloc[-1]})")


if __name__ == "__main__":
    main()