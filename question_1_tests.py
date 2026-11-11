"""
Jack Kjar
CSE 163 AE
This file produces a scatter plot based on a small, testing dataset, in order
to test my plot from research question 1.
"""
import pandas as pd
import plotly.express as px


def main():
    """
    Produces a test plot to verify the research question 1 plot is correct.
    """
    injuries = pd.read_csv("test_injuries.csv")
    out_injuries = injuries[injuries["report_status"] == "Out"]
    out_injuries = out_injuries.groupby("season").size()
    out_injuries = out_injuries.reset_index()
    out_injuries.rename(columns={0: "Out Designations"}, inplace=True)

    graph = px.scatter(out_injuries, x="season", y="Out Designations",
                       title="Out Designations per Season", trendline="ols")
    graph.write_html("test_injuries_over_time.html")


if __name__ == "__main__":
    main()
