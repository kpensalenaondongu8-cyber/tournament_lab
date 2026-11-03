import json

def list_teams():
    with open("standings.json", "r") as file:
        data = json.load(file)
        print("--- this are the teams that registered for the tournament ---")
        for teams in data:
            team_names = teams['name']
            print(f"{team_names}")
