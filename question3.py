"""
Name: Shreyas Sao
Section: <your section>

Find the NFL positions with the highest and lowest injury rates.
"""

import pandas as pd
import plotly.express as px


def main() -> None:
    """
    Prints the number of reported injuries for each position, sorted
    from most to fewest, followed by the positions with the most and
    fewest. A player is counted once per season and week.
    """

    injuries = pd.read_csv("cleaned_injuries.csv")

    has_position = injuries["position"].str.strip() != ""
    valid = injuries[has_position]

    counts = valid["position"].value_counts()

    print(counts)
    print(f"\nMost injuries: {counts.index[0]} ({counts.iloc[0]})")
    print(f"Fewest injuries: {counts.index[-1]} ({counts.iloc[-1]})")

    fig = px.bar(
        x=counts.index,
        y=counts.values,
        labels={"x": "Position", "y": "Number of Injuries"},
        title="Injuries by Position",
    )
    fig.write_html("injuries_by_position.html")


if __name__ == "__main__":
    main()
