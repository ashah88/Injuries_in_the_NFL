"""
Name: Shreyas Sao
Section: <your section>

Find the NFL positions with the highest and lowest injury rates.
"""

import pandas as pd
import plotly.express as px


def count_injuries(injuries: pd.DataFrame) -> pd.Series:
    """
    Returns the number of reported injuries for each position, sorted
    from most to fewest. Rows with a blank or missing position are
    ignored.
 
    Parameters:
        injuries: DataFrame of injury reports with a "position" column
    """
    has_position = injuries["position"].str.strip() != ""
    valid = injuries[has_position]
    return valid["position"].value_counts()

def plot_injuries(counts: pd.Series) -> px.bar:
    """
    Returns a bar chart of the number of reported injuries for each
    position, in the same order as the given counts.
 
    Parameters:
        counts: number of injuries for each position, indexed by
                position
    """
    return px.bar(
        x=counts.index,
        y=counts.values,
        title="Reported NFL Injuries by Position",
        labels={"x": "Position", "y": "Number of Injuries"}
    )

def main() -> None:
    injuries = pd.read_csv("cleaned_injuries.csv")
    counts = count_injuries(injuries)
 
    print(counts)
    print(f"\nMost injuries: {counts.index[0]} ({counts.iloc[0]})")
    print(f"Fewest injuries: {counts.index[-1]} ({counts.iloc[-1]})")
 
    fig = plot_injuries(counts)
    fig.write_html("injuries_by_position.html")


if __name__ == "__main__":
    main()
