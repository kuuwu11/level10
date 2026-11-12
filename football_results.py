# read the football data from cfb.csv using pandas
import pandas as pd

football_data = pd.read_csv("cfb.csv")

# ask user which season they would like to analyze
# allow the user to select a season
season = int(input("Enter a season to analyze: "))

# filter the data to include only teams from the selected season
# work with any season included in the CSV file
season_data = football_data[football_data["Season"] == season]

# let the user know if the requested season is not found
if season_data.empty:
    print("Season not found.")

else:
    print(f"College Football Results for {season}")

    # use a dictionary to organize the teams into the four win categories
    # organize the teams from that season into four categories:
    win_categories = {
        "10 or more wins": [],
        "8-9 wins": [],
        "6-7 wins": [],
        "Fewer than 6 wins": [],
    }

    # use loops and selection to process the teams
    # avoid hard-coding the team names or results
    for index, row in season_data.iterrows():
            team = row["Team"]
            wins = row["Win"]

            if wins >= 10:
                win_categories["10 or more wins"].append(team)
            elif wins >= 8:
                win_categories["8-9 wins"].append(team)
            elif wins >= 6:
                win_categories["6-7 wins"].append(team)
            else:
                win_categories["Fewer than 6 wins"].append(team)

    # display the teams in each category clearly for the user.
    for category, teams in win_categories.items():
        print(f"\n{category}:")
        for team in teams:
            print(team)
        