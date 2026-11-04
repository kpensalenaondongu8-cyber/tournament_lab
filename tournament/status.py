import json

def update_match_status(match_id, new_status):
    with open("tournament.json", "r") as file:
        data = json.load(file)
    
    for fixture in data.get("fixtures", []):
        if fixture["id"] == match_id:
            fixture["status"] = new_status  
            break
            
    with open("tournament.json", "w") as file:
        json.dump(data, file, indent=4)
