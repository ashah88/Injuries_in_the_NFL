import pandas as pd
import plotly.express as px

GAMES_FILE = 'cleaned_games.csv'
INJURIES_FILE = 'cleaned_injuries.csv'


def count_outs(injuries):
    outs = injuries[injuries['report_status'] == 'Out']
    groups = outs.groupby(['season', 'team', 'week'])

    num_injuries = groups.size().rename('injuries')
    num_injuries = num_injuries.reset_index()
    
    return num_injuries


def team_rest(games):
    home = games[['game_id', 'season', 'week', 'home_team', 'home_rest']]
    home = home.rename(columns={'home_team': 'team', 'home_rest': 'rest_days'})

    away = games[['game_id', 'season', 'week', 'away_team', 'away_rest']]
    away = away.rename(columns={'away_team': 'team', 'away_rest': 'rest_days'})
    
    return pd.concat([home, away])


def match_injuries_to_games(outs, rest):
    merged = rest.merge(outs, on=['season', 'team', 'week'], how='left')
    merged['injuries'] = merged['injuries'].fillna(0)
    
    return merged


def plot_injuries_by_rest(merged):
    groups = merged.groupby('rest_days')
    group_by_rest = groups['injuries'].agg(['mean', 'count'])
    group_by_rest = group_by_rest.reset_index()

    fig = px.bar(group_by_rest, x='rest_days', y='mean', hover_data=['count'], labels={'rest_days': 'Days of rest before game', 'mean': 'Average injuries per game', 'count': 'Number of games'}, title="Injuries per Game by Days of Rest (2012-2025)")

    fig.write_html('rq2_rest_days.html')

    return group_by_rest

def plot_games_by_rest(rest):
    games = rest['rest_days'].value_counts().rename('games')
    games = games.reset_index()

    fig = px.bar(games, x='rest_days', y='games', labels={'rest_days': 'Days of rest before the game', 'games': 'Number of games (one per team)'}, title="Number of Games Played on Each Number of Rest Days (2012-2025)")
    
    fig.write_html('rq2_games_by_rest.html')
    return games


def main():
    games = pd.read_csv(GAMES_FILE)
    injuries = pd.read_csv(INJURIES_FILE)

    outs = count_outs(injuries)
    rest = team_rest(games)
    merged = match_injuries_to_games(outs, rest)
    plot_injuries_by_rest(merged)
    plot_games_by_rest(rest)


if __name__ == '__main__':
    main()