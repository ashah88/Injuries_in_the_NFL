import pandas as pd

URL = 'https://github.com/nflverse/nflverse-data/releases/download/'
GAMES_URL = ('https://raw.githubusercontent.com/nflverse/nfldata/master/'
             'data/games.csv')
SEASONS = range(2012, 2026)


def combine(folder, prefix):
    """
    Reads {prefix}_{season}.csv for every season from the given nflverse
    release folder and stacks them into one DataFrame.
    """
    frames = [pd.read_csv(f'{URL}{folder}/{prefix}_{season}.csv',
                          low_memory=False)
              for season in SEASONS]
    return pd.concat(frames, ignore_index=True)


def main():
    combine('injuries', 'injuries').to_csv('data/injuries.csv', index=False)
    combine('rosters', 'roster').to_csv('data/rosters.csv', index=False)
    pd.read_csv(GAMES_URL).to_csv('data/games.csv', index=False)


if __name__ == '__main__':
    main()