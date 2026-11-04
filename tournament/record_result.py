import json

def record_result(match_id, new_homescore, new_away_score):
    with open("tournament.json", "r") as file:
        data = json.load(file)
        
        result = data.get('fixtures')
        
        print(result)         
        result['home_score']= new_homescore
        result['away_score'] = new_away_score
    with open("tournament.json", "w") as file:
        json.dump(data, file, indent=4)