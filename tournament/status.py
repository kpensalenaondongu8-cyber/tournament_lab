from validate import validate_status
import json

def update_match_status(match_id, new_status):
    is_valid, validation_result = validate_status(new_status)
    if not is_valid:
        return validation_result
    cleaned = validation_result

    with open("tournament.json", "r") as file:
        data = json.load(file)

    fixture = data.get("fixtures")
    match_found = True

    for fixtures in fixture:
        if fixtures["id"] == match_id:
            fixtures["status"] = cleaned 
            break
    if not match_found:
        return f"Error: match_id '{match_id}' not found."  
         
    with open("tournament.json", "w") as file:
        json.dump(data, file, indent=4)
        return "status updated succesfully."
