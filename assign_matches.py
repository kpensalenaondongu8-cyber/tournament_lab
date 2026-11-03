import json

def generate_tournament_data():
    filename = "tournament.json"
    
    with open(filename, "r") as file:
        tournament_data = json.load(file)
    
    teams = tournament_data["team"]
    num_teams = len(teams)
    
    if 'fixtures' not in tournament_data:
        tournament_data["fixtures"] = []
    
    for i in range(num_teams):
        team1 = teams[i]["name"]
        
        for j in range(i + 1, num_teams):
            team2 = teams[j]["name"]
            
            fixture = { 
                "home_team": team1,
                "away_team": team2,
                "match": f"{team1} vs {team2}"
            }
            
            tournament_data["fixtures"].append(fixture)
            
    with open(filename, "w") as file:
        json.dump(tournament_data, file, indent=4)
        print("Tournament fixtures successfully generated and saved!")

