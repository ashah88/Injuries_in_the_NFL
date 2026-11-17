'''
Ajay Shah
CSE 163
This file tests the functions and plots in question2.py using
test_games.csv.
'''
import os

import pandas as pd

import question2

TEST_GAMES = 'test_games.csv'

# Test plots are saved under these names so the real charts are not
# overwritten.
TEST_INJURIES_PLOT = 'test_rq2_rest_days.html'
TEST_GAMES_PLOT = 'test_rq2_games_by_rest.html'


def make_injuries() -> pd.DataFrame:
    '''
    Returns a small DataFrame of injuries for the teams in test_games.csv
    '''
    return pd.DataFrame({
        'season': [2024, 2024, 2024, 2024],
        'team': ['KC', 'KC', 'NO', 'LA'],
        'week': [7, 7, 7, 7],
        'report_status': ['Out', 'Out', 'Out', 'Questionable'],
    })


def test_team_rest(games: pd.DataFrame) -> None:
    '''
    Tests the team_rest method in question2.py
    '''
    rest = question2.team_rest(games)

    assert len(rest) == 6

    game = rest[rest['game_id'] == '2024_07_LA_KC']
    kc = game[game['team'] == 'KC']
    la = game[game['team'] == 'LA']
    assert kc['rest_days'].iloc[0] == 4
    assert la['rest_days'].iloc[0] == 12


def test_plot_injuries_by_rest(games: pd.DataFrame) -> None:
    '''
    Tests the plot_injuries_by_rest method in question2.py
    '''
    outs = question2.count_outs(make_injuries())
    rest = question2.team_rest(games)
    merged = question2.match_injuries_to_games(outs, rest)
    fig = question2.plot_injuries_by_rest(merged, TEST_INJURIES_PLOT)

    bars = fig.data[0]
    heights = dict(zip(bars.x, bars.y))
    assert list(bars.x) == [4, 7, 12]
    assert heights[4] == 1.5
    assert heights[7] == 1.0
    assert heights[12] == 0.0

    assert list(bars.customdata[:, 0]) == [2, 3, 1]

    assert fig.layout.title.text == \
        'Injuries per Game by Days of Rest (2012-2025)'
    assert fig.layout.xaxis.title.text == 'Days of rest before game'
    assert fig.layout.yaxis.title.text == 'Average injuries per game'

    assert os.path.exists(TEST_INJURIES_PLOT)


def test_plot_games_by_rest(games: pd.DataFrame) -> None:
    '''
    Tests the games-by-rest method in question2.py
    '''
    rest = question2.team_rest(games)
    fig = question2.plot_games_by_rest(rest, TEST_GAMES_PLOT)

    bars = fig.data[0]
    heights = dict(zip(bars.x, bars.y))
    assert heights[7] == 3
    assert heights[4] == 2
    assert heights[12] == 1

    assert sum(bars.y) == 6

    assert fig.layout.xaxis.title.text == 'Days of rest before the game'
    assert fig.layout.yaxis.title.text == 'Number of games (one per team)'
    assert os.path.exists(TEST_GAMES_PLOT)


def main():
    games = pd.read_csv(TEST_GAMES)
    test_team_rest(games)
    test_plot_injuries_by_rest(games)
    test_plot_games_by_rest(games)
    print('All tests passed')


if __name__ == '__main__':
    main()