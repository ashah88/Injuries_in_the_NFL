import pandas as pd

import question2

TEST_FILE = 'test_games.csv'

def test_team_rest(games):
    rest = question2.team_rest(games)

    assert len(rest) == 6

    assert (rest['game_id'].value_counts() == 2).all()

    game = rest[rest['game_id'] == '2024_07_LA_KC']
    kc = game[game['team'] == 'KC']
    la = game[game['team'] == 'LA']
    assert kc['rest_days'].iloc[0] == 4
    assert la['rest_days'].iloc[0] == 12


def test_plot_games_by_rest(games):
    rest = question2.team_rest(games)
    # Have to fix
    #counts = question2.count_games_by_rest(rest)
    counts = counts.set_index('rest_days')['games']
 
    assert counts[7] == 3
    assert counts[4] == 2
    assert counts[12] == 1
    assert counts.sum() == 6


def main():
    games = pd.read_csv(TEST_FILE)
    test_team_rest(games)
    test_plot_games_by_rest(games)
    print('All tests passed')


if __name__ == "__main__":
    main()