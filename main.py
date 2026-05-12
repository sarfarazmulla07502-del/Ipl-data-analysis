import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, 'data')
CHARTS_DIR = os.path.join(BASE_DIR, 'charts')
MATCHES_PATH = os.path.join(DATA_DIR, 'matches.csv')
DELIVERIES_PATH = os.path.join(DATA_DIR, 'deliveries.csv')


def load_csv(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Required data file not found: {path}\n"
            "Please place the IPL dataset under the project data/ directory."
        )
    return pd.read_csv(path)


def main() -> None:
    matches = load_csv(MATCHES_PATH)
    deliveries = load_csv(DELIVERIES_PATH)

    print('Matches sample:')
    print(matches.head(), '\n')
    print('Deliveries sample:')
    print(deliveries.head(), '\n')

    csk_matches = matches[matches['winner'] == 'Chennai Super Kings']
    print('CSK wins sample:')
    print(csk_matches.head(), '\n')

    team_wins = matches['winner'].value_counts()
    print('Team win counts:')
    print(team_wins, '\n')

    top_batsmen = deliveries.groupby('batter')['batsman_runs'].sum()
    top_batsmen = top_batsmen.sort_values(ascending=False)
    print('Top 10 run scorers:')
    print(top_batsmen.head(10), '\n')

    total_matches = matches['team1'].value_counts() + matches['team2'].value_counts()
    wins = matches['winner'].value_counts()
    win_percentage = (wins / total_matches) * 100
    print('Win percentage by team:')
    print(win_percentage.sort_values(ascending=False), '\n')

    os.makedirs(CHARTS_DIR, exist_ok=True)
    plt.figure(figsize=(12, 6))
    team_wins.plot(kind='bar')
    plt.title('IPL Team Wins Comparison')
    plt.xlabel('Teams')
    plt.ylabel('Wins')
    plt.xticks(rotation=45)
    plt.tight_layout()
    chart_path = os.path.join(CHARTS_DIR, 'team_wins.png')
    plt.savefig(chart_path)
    print(f'Chart saved to: {chart_path}')
    plt.close()


if __name__ == '__main__':
    main()
