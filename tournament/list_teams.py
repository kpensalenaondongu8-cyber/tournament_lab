import json

def list_teams():
    with open("tournament.json", "r") as file:
        data = json.load(file)
        print("--- this are the teams that registered for the tournament ---")
        result = data.get('teams', [])
        for teams in result:
            team_names = teams['name']
            print(f"{team_names}")
