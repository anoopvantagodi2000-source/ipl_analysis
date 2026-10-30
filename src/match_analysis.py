import csv
import matplotlib.pyplot as plt
from collections import defaultdict

MATCH_CSV_PATH = "resources/matches.csv"
DELIVERIES_PATH = "./resources/deliveries.csv"
matches_data = {}

def calculate(path : str):
    try:
        with open(path,'r',encoding="utf-8") as matches_csv:
            matches = csv.DictReader(matches_csv)
            for match in matches:
                year = match.get("season")
                team1 = match.get("team1")
                team2 = match.get("team2")
                if not year or not team1 or not team2:
                    continue


                if year not in matches_data:
                    matches_data[year] = defaultdict(int)

                matches_data[year][team1]= matches_data[year][team1] + 1
                matches_data[year][team2] = matches_data[year][team2] + 1
                matches_data[year]["total_matches"] = matches_data[year]["total_matches"]+1



    except FileNotFoundError:
        raise FileNotFoundError(f"file not found {path}")
    except OSError:
        raise OSError("permission denied")

    return matches_data

def fetch_number_of_matches_won_by_each_team(path : str):
    match_data = {}
    try:
        with open(path,'r',encoding="utf-8") as csv_file:
            rows = csv.DictReader(csv_file)
            for row in rows:
                year = row["season"]
                winner = row["winner"]
                if not year or not winner:
                    continue
                if year not in match_data:
                    match_data[year] = defaultdict(int)
                match_data[year][winner] += 1
    except FileNotFoundError:
        raise FileNotFoundError(f"file is not found @ {path}")
    except OSError:
        raise OSError("permission denied")
    return match_data


def fetch_extra_runs_conceded_by_year(path_of_matches:str,path_of_deliveries:str, year: str):
    #get match id from the given year
    match_ids = set()
    with open(path_of_matches,'r',encoding="utf-8") as match_csv:
        matches = csv.DictReader(match_csv)
        for match in matches:
            if match["season"] == year:
                match_ids.add(match["id"])
    extra_deliveries = defaultdict(int)
    with open(path_of_deliveries,'r',encoding= "utf-8") as del_csv:
        deliveries = csv.DictReader(del_csv)
        for delivery in deliveries:
            if delivery["match_id"] in match_ids:
                team = delivery["bowling_team"]
                extra_deliveries[team] += int(delivery["extra_runs"])
    return extra_deliveries

def fetch_economical_bowler_in_year(path_of_matches:str,path_of_deliveries:str, year: str):
    match_ids = set()
    with open(path_of_matches,'r',encoding="utf-8") as match_csv:
        matches = csv.DictReader(match_csv)
        for match in matches:
            if match["season"] == year:
                match_ids.add(match["id"])
    bowler_run_conceded = defaultdict(int)
    total_ball_bowled = defaultdict(int)
    with open(path_of_deliveries,'r',encoding= "utf-8") as del_csv:
        deliveries = csv.DictReader(del_csv)
        for delivery in deliveries:
            if delivery["match_id"] in match_ids:
                bowler = delivery["bowler"]
                bowler_run_conceded[bowler] += int(delivery["total_runs"])-int(delivery["bye_runs"]) - int(delivery["legbye_runs"])-int(delivery["penalty_runs"])
                wide = int(delivery["wide_runs"])
                no_ball = int(delivery["noball_runs"])
                if wide == 0 and no_ball == 0:
                   total_ball_bowled[bowler] += 1

    economy_of_bowler = {}
    for bowler in bowler_run_conceded.keys():
        economy_of_bowler[bowler] = round(bowler_run_conceded[bowler]/total_ball_bowled[bowler],2)

    return economy_of_bowler









def plot(data: dict):
    if not data:
        print("No data exists")
        return

    years = sorted(list(data.keys()))
    teams = set()
    for year in years:
        teams.update(team for team in data[year] if team != "total_matches")

    fig, ax = plt.subplots()

    bottom = [0] * len(years)

    for team in teams:
        counts = [data[year].get(team, 0) for year in years]

        ax.bar(years, counts, bottom=bottom, label=team)

        bottom = [bottom[i] + counts[i] for i in range(len(years))]

    ax.set_title("Matches Played by Team by Season")
    ax.set_xlabel("Season")
    ax.set_ylabel("Matches Played")
    ax.legend()
    plt.savefig('images/4.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_number_of_matches_played_per_year(data:dict):
    years = sorted(list(data.keys()))
    total_matches_played_per_season = [data[year]["total_matches"] for year in years]

    fig,ast = plt.subplots()
    ast.bar(years, total_matches_played_per_season)
    ast.set_title("total number of matches played in each year")
    ast.set_xlabel("Years")
    ast.set_ylabel("Scores")

    plt.setp(ast.get_xticklabels(), ha="right")
    fig.tight_layout()
    plt.savefig('images/5.png', dpi=300, bbox_inches='tight')

    plt.show()


def plot_stack_graph(data:dict):
    years = sorted(list(data.keys()))
    teams = set()
    for year in years:
        teams.update(team for team in data[year])


    fig,ax = plt.subplots()
    bottom = [0] * len(years)

    for team in teams:
        counts = [data[year].get(team, 0) for year in years]

        ax.bar(years, counts, bottom=bottom, label=team)

        bottom = [bottom[i] + counts[i] for i in range(len(years))]

    ax.set_title("Matches won by each team")
    ax.set_xlabel("Year")
    ax.set_ylabel("Matches Won")
    ax.legend()

    plt.savefig('images/6.png', dpi=300, bbox_inches='tight')

def plot_extra_runs_conceded(data : dict):
    sorted_data = sorted(data.items(),key= lambda item : item[1])
    teams = [team for team,_ in sorted_data]
    extra_runs = [runs for _,runs in sorted_data]
    fig,ast = plt.subplots()
    ast.bar(teams,extra_runs)
    ast.set_title("Extra runs conceded in year 2016")
    ast.set_xlabel("teams")
    ast.set_ylabel("Extra Runs")

    ast.tick_params(axis="x", labelrotation=45)
    plt.setp(ast.get_xticklabels(), ha="right")
    fig.tight_layout()
    plt.savefig('images/7.png', dpi=300, bbox_inches='tight')

    plt.show()



def plot_economical_bowler(data : dict):
    sorted_data = sorted(data.items(),key= lambda item : item[1])
    bowler_names = [bowler for bowler,_ in sorted_data][:10]
    extra_runs = [runs for _,runs in sorted_data][:10]
    fig,ast = plt.subplots()
    ast.bar(bowler_names,extra_runs)
    ast.set_title("Top 10 Economical bowlers year 2015")
    ast.set_xlabel("Bowlers")
    ast.set_ylabel("runs conceded")

    ast.tick_params(axis="x", labelrotation=45)
    plt.setp(ast.get_xticklabels(), ha="right")
    fig.tight_layout()
    plt.savefig('images/8.png', dpi=300, bbox_inches='tight')
    plt.show()





def execute():
    data = calculate(MATCH_CSV_PATH)
    plot(data)
    # data = calculate(MATCH_CSV_PATH)
    # plot_number_of_matches_played_per_year(data)
    #
    # data = fetch_number_of_matches_won_by_each_team(MATCH_CSV_PATH)
    # plot_stack_graph(data)
    #
    # data = fetch_extra_runs_conceded_by_year(MATCH_CSV_PATH,DELIVERIES_PATH,"2016")
    # plot_extra_runs_conceded(data)
    #
    # data = fetch_economical_bowler_in_year(MATCH_CSV_PATH, DELIVERIES_PATH, "2015")
    # plot_economical_bowler(data)



execute()



