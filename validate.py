def validate_team(name, registered_names):
    cleaned_name = name.strip()

    if not cleaned_name:
        return False, "Error: Team name cannot be blank."
    
    if len(cleaned_name) < 2:
        return False, "Error: Team name must be more than 2 characters."
    if len(cleaned_name) > 30:
        return False, "Error: Team name must cannot exceed 30 characters"
    
    for teams in registered_names:
        if teams['name'].strip().lower() == cleaned_name.lower():
            return False, f"Error:'{teams['name']}' is rejected as duplicate"
        
    return True, cleaned_name    
        