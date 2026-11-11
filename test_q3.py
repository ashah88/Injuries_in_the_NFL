import pandas as pd

from question3 import count_injuries, plot_injuries


def test_count_injuries_counts(injuries: pd.DataFrame) -> None:
    """
    Tests the function count_injuries for the number of injuries
    counted for each position.
    """
    counts = count_injuries(injuries)
    assert counts["WR"] == 4
    assert counts["RB"] == 3
    assert counts["QB"] == 2
    assert counts["TE"] == 1
    assert counts["LB"] == 1
    assert counts["P"] == 1


def test_count_injuries_order(injuries: pd.DataFrame) -> None:
    """
    Tests the function count_injuries for sorting from most to fewest
    injuries. TE, LB, and P are tied for fewest, so only the order of
    the first three positions is checked.
    """
    counts = count_injuries(injuries)
    assert list(counts.index[:3]) == ["WR", "RB", "QB"]
    assert set(counts.index[3:]) == {"TE", "LB", "P"}
    assert counts.index[0] == "WR"
    assert counts.iloc[-1] == 1


def test_count_injuries_total(injuries: pd.DataFrame) -> None:
    """
    Tests the function count_injuries for counting every row in the
    file, since none of the 12 rows have a blank position. There
    should be 6 positions and 12 counted injuries.
    """
    counts = count_injuries(injuries)
    assert len(counts) == 6
    assert counts.sum() == 12


def test_count_injuries_no_change(injuries: pd.DataFrame) -> None:
    """
    Tests the function count_injuries for not modifying the DataFrame
    that is passed in.
    """
    before = injuries.copy()
    count_injuries(injuries)
    assert injuries.equals(before)
    assert len(injuries) == 12

def test_plot_injuries(injuries: pd.DataFrame) -> None:
    """
    Tests the function plot_injuries by saving the bar chart for the
    small dataset to test_injuries_by_position.html so it can be
    checked by hand. The chart should show one bar per position with
    these heights, from left to right: WR 4, RB 3, QB 2, and then
    TE 1, LB 1, and P 1 in any order.
    """
    counts = count_injuries(injuries)
    fig = plot_injuries(counts)
    fig.write_html("test_injuries_by_position.html")

def main() -> None:
    injuries = pd.read_csv("test_injuries.csv")
    test_count_injuries_counts(injuries)
    test_count_injuries_order(injuries)
    test_count_injuries_total(injuries)
    test_count_injuries_no_change(injuries)
    test_plot_injuries(injuries)
    print("All tests passed!")


if __name__ == "__main__":
    main()