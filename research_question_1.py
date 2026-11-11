"""
Jack Kjar
CSE 163 AE
This file contains a script that creates a plot to answer research question 1.
"""
import pandas as pd
import plotly.express as px


def main():
    """
    Creates a plotly scatter plot showing the number of out designations
    per season in the NFL between 2012 and 2025.
    """
    injuries = pd.read_csv("cleaned_injuries.csv")
    out_injuries = injuries[injuries["report_status"] == "Out"]
    out_injuries = out_injuries.groupby("season").size()
    out_injuries = out_injuries.reset_index()
    out_injuries.rename(columns={0: "Out Designations"}, inplace=True)

    graph = px.scatter(out_injuries, x="season", y="Out Designations",
                       title="Out Designations per Season (2012-2025)",
                       trendline="ols")
    graph.write_html("injuries_over_time.html")


if __name__ == "__main__":
    main()
