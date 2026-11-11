import pandas as pd

from question3 import count_injuries, plot_injuries




def test_plot_injuries(injuries: pd.DataFrame) -> None:
    """
    Behavior:
        Tests the function plot_injuries by saving the bar chart for
        the small dataset to the current directory so it can
        be checked by hand. The chart should show one bar per
        position.
    Parameters:
        injuries - DataFrame of the small test dataset
    """
    counts = count_injuries(injuries)
    fig = plot_injuries(counts)
    fig.write_html("test_injuries_by_position.html")


def main() -> None:
    injuries = pd.read_csv("test_injuries.csv")
    test_plot_injuries(injuries)
    print("All tests passed!")


if __name__ == "__main__":
    main()
