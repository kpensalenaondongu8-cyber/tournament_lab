from validate import validate_team
import json

def register_team(team_name):
    file_name = "tournament.json"
    with open(file_name, "r") as file:
        data = json.load(file)
        
    teams_list = data.get("teams")
    
    is_valid, validation_result = validate_team(team_name, teams_list)

    if not is_valid:
        return validation_result
    
    validated_name = validation_result
    
    next_id = len(teams_list) + 1
    team_id = f"TM{next_id:03d}"  
    
    new_team = {
        "id": team_id,
        "name": validated_name
    }
    
    if "teams" not in data:
        data["teams"] = [] 
        
    data["teams"].append(new_team)
    
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
        
    return f"Success: {validated_name} successfully registered for the tournament with ID {team_id}."
