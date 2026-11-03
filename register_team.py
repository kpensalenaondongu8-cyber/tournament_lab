from validate import validate_team
import json

def register_team(team_name):
    with open("standings.json", "r") as file:
        data = json.load(file)
        
        is_valid, validation_result = validate_team(team_name, data)

        if not is_valid:
            return validation_result
        
        name = validation_result
        next_id = len(data)+1
        team_id = f"TM{next_id:03d}"

        registered_team = {
            "id": team_id,
            "name": name
        }
        data.append(registered_team)
    with open("standings.json", "w") as file:
        json.dump(data, file, indent=4)
    return(f"{team_name} successfully registered for the tournament.")        
    
