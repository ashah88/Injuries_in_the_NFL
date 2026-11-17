'''
Ajay Shah
CSE 163
This file contains a script that creates a plot to answer research question 2.
'''
import pandas as pd
import plotly.express as px

# GAMES_FILE: str = "cleaned_games.csv"
# INJURIES_FILE: str = "cleaned_injuries.csv"
DATA_FILE: str = "games_and_injuries.csv"

# def count_outs(injuries: pd.DataFrame)->pd.DataFrame:
#     '''
#     Given a Pandas DataFrame of NFL injuries, counts how many "Out" designations each team had in each week, using the season, team, and week columns. Returns a Pandas DataFrame with the year, team, week, and number of "Out" designations the team had that week.
#     '''
#     outs = injuries[injuries['report_status'] == 'Out']
#     groups = outs.groupby(['season', 'team', 'week'])

#     num_injuries = groups.size().rename("injuries")
#     num_injuries = num_injuries.reset_index()

#     return num_injuries


# def team_rest(games: pd.DataFrame) -> pd.DataFrame:
#     '''
#     Given a Pandas DataFrame of NFL games, splts each game into a row of the home team and a row for the away team because each team can different days of rest. Returns a Pandas DataFrame with the game ID, season, week, team, and number of days of rest that team had before the game.
#     '''
#     home = games[['game_id', 'season', 'week', 'home_team', 'home_rest']]
#     home = home.rename(columns={'home_team': 'team', 'home_rest': 'rest_days'})

#     away = games[['game_id', 'season', 'week', 'away_team', 'away_rest']]
#     away = away.rename(columns={'away_team': 'team', 'away_rest': 'rest_days'})

#     rest = pd.concat([home, away])

#     return rest


# def match_injuries_to_games(outs: pd.DataFrame, rest: pd.DataFrame) -> pd.DataFrame:
#     '''
#     Given a Pandas DataFrame of the number of "Out" designations and a Pandas DataFrame of the number of rest days each team has, matches each team's injuries to the game it played that week using the season, team, and week columns. Returns a Pandas DataFrame with one row per team per game, with the team's rest days and the number of injuries the team had.
#     '''
#     merged = rest.merge(outs, on=['season', 'team', 'week'], how='left')
#     merged['injuries'] = merged['injuries'].fillna(0)
#     merged.to_csv("games_and_injuries.csv")

#     return merged


def plot_injuries_by_rest(merged: pd.DataFrame,
                          file_name: str = 'q2_rest_days.html') -> px.bar:
    '''
    Given a Pandas DataFrame with the injuries and rest days merged, makes a
    bar graph of the average number of injuries per game for each number of
    rest days and saves it as a Plotly figure. Returns a Plotly figure.
    '''
    groups = merged.groupby('rest_days')
    group_by_rest = groups['injuries'].agg(['mean', 'count'])
    group_by_rest = group_by_rest.reset_index()

    fig = px.bar(
        group_by_rest,
        x="rest_days",
        y="mean",
        hover_data=["count"],
        labels={
            "rest_days": "Days of rest before game",
            "mean": "Average injuries per game",
            "count": "Number of games",
        },
        title="Injuries per Game by Days of Rest (2012-2025)",
    )

    fig.write_html(file_name)

    return fig


def plot_injuries_by_team(merged: pd.DataFrame,
                          file_name: str = "q2_team_injuries.html") -> px.bar:
    '''
    Given a Pandas DataFrame with the injuries and teams merged, makes a
    bar graph of the average number of injuries per game for each team
    and saves it as a Plotly figure. Returns a Plotly figure.
    '''
    groups = merged.groupby('team')
    group_by_team = groups['injuries'].agg(['mean', 'count'])
    group_by_team = group_by_team.reset_index()

    fig = px.bar(
        group_by_team,
        x="team",
        y="mean",
        hover_data=["count"],
        labels={
            "team": "Team",
            "mean": "Average injuries per game",
            "count": "Number of games",
        },
        title="Injuries per Game by Team (2012-2025)",
    )

    fig.write_html(file_name)

    return fig

# def plot_games_by_rest(rest: pd.DataFrame, file_name: str = 'rq2_games_by_rest.html') -> px.bar:
#     '''
#     Given a Pandas DataFrame of the team rest days, makes a bar graph of the number of games played on each number of rest days and saves it as a Plotly figure.
#     Each game is counted twice, once for each team.
#     Returns a Plotly figure.
#     '''
#     games = rest['rest_days'].value_counts().rename('games')
#     games = games.reset_index()

#     fig = px.bar(games, x='rest_days', y='games', labels={'rest_days': 'Days of rest before the game', 'games': 'Number of games (one per team)'}, title="Number of Games Played on Each Number of Rest Days (2012-2025)")

#     fig.write_html(file_name)
#     return fig


def main() -> None:
    # games = pd.read_csv(GAMES_FILE)
    # injuries = pd.read_csv(INJURIES_FILE)
    data = pd.read_csv(DATA_FILE)

    # outs = count_outs(injuries)
    # rest = team_rest(games)
    # merged = match_injuries_to_games(outs, rest)
    plot_injuries_by_rest(data)
    plot_injuries_by_team(data)
    # plot_games_by_rest(rest)


if __name__ == "__main__":
    main()
