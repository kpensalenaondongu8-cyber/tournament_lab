MATCH_STATUS = ["pending", "ongoing", "finished"]


def validate_team(name, registered_names):
    cleaned_name = name.strip()

    if not cleaned_name:
        return False, "Error: Team name cannot be blank."
    
    if len(cleaned_name) < 2:
        return False, "Error: Team name must be 2 or more characters."
    if len(cleaned_name) > 30:
        return False, "Error: Team name cannot exceed 30 characters."
    
    for team in registered_names:
        if team['name'].strip().lower() == cleaned_name.lower():
            return False, f"Error: '{team['name']}' is rejected as a duplicate."
        
    return True, cleaned_name


def validate_status(new_status):
    cleaned = str(new_status).strip().lower()
    
    for result in MATCH_STATUS:
        if cleaned.lower() not in MATCH_STATUS:
            return False, "Error: Invalid status"
        return True, cleaned

            