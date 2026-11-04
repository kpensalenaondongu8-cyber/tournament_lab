import json

def record_result(fix_id, new_homescore, new_away_score):
    with open("tournament.json", "r") as file:
        data = json.load(file)
        
        for result in data.get('fixtures'):
            if result['id'] == fix_id:
               result['home_score']= new_homescore
               result['away_score'] = new_away_score
               break
        with open("tournament.json", "w") as file:
            json.dump(data, file, indent=4)