import json

def calculate_standings():
    
    with open("tournament.json", "r", encoding="utf-8") as file:
            data = json.load(file)

    teams_list = data.get("teams")
    fixtures_list = data.get("fixtures")

    standings = {}
    for team in teams_list:
        standings[team["name"]] = {
            "MP": 0,   
            "W": 0,   
            "D": 0,    
            "L": 0, 
            "GF": 0,   
            "GA": 0,   
            "GD": 0,   
            "PTS": 0  
        }

    for match in fixtures_list:
        if match.get("status") == "played" or (match.get("home_score") is not None and match.get("away_score") is not None):
            home = match["home"]
            away = match["away"]
            h_score = int(match["home_score"])
            a_score = int(match["away_score"])

            if home not in standings or away not in standings:
                continue

            standings[home]["MP"] += 1
            standings[away]["MP"] += 1

            standings[home]["GF"] += h_score
            standings[home]["GA"] += a_score

            standings[away]["GF"] += a_score
            standings[away]["GA"] += h_score

            if h_score > a_score: 
                standings[home]["W"] += 1
                standings[home]["PTS"] += 3
                standings[away]["L"] += 1
                
            elif a_score > h_score:  
                standings[away]["W"] += 1
                standings[away]["PTS"] += 3
                standings[home]["L"] += 1
                
            else:  
                standings[home]["D"] += 1
                standings[away]["D"] += 1
                standings[home]["PTS"] += 2
                standings[away]["PTS"] += 2

    ranked_table = []
    for team_name, stats in standings.items():
        stats["GD"] = stats["GF"] - stats["GA"]
        
        team_entry = {"name": team_name, **stats}
        ranked_table.append(team_entry)

    ranked_table.sort(key=lambda x: (x["PTS"], x["GD"], x["GF"]), reverse=True)

    return ranked_table


def display_standings():
    table = calculate_standings()
    if isinstance(table, str):
        return table

    header = f"{'Pos':<4}{'Team':<18}{'MP':<4}{'W':<4}{'D':<4}{'L':<4}{'GF':<4}{'GA':<4}{'GD':<4}{'PTS':<4}"
    divider = "-" * len(header)
    
    lines = [header, divider]
    for index, team in enumerate(table, start=1):
        line = (f"{index:<4}{team['name']:<18}{team['MP']:<4}{team['W']:<4}"
                f"{team['D']:<4}{team['L']:<4}{team['GF']:<4}{team['GA']:<4}"
                f"{team['GD']:<+4}{team['PTS']:<4}")
        lines.append(line)
        
    return "\n".join(lines)
