import json

def list_fixtures():
    with open("tournament.json", "r") as file:
        data = json.load(file)
        
        print("---- Fixtures ----")
        result = data.get('fixtures')

        for all in result:
            print(all['match'])