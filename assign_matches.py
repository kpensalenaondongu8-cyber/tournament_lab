
import json


def generate_tournament_fixture():
    with open("tournament.json", "r") as file:
        data = json.load(file)


        if 'fixtures' not in data:
            data['fixtures'] = []
        teams = data.get('teams')
        all_teams = len(teams)
        next_id = len(data['fixtures'])+1
        fixture_id = f"M{next_id:03d}"

        for i in range(all_teams):
            team1 = teams[i]['name']

            for j in range(i + 1, all_teams):
                team2 = teams[j]['name']

                fixtures = {
                    "id": fixture_id,
                    "home": team1,
                    "away": team2,
                    "match": f"{team1} Vs {team2}",
                    "status": "pending",
                    "home_score": None,
                    "away_score": None
                }   
                data['fixtures'].append(fixtures)

        with open("tournament.json", "w") as file:
            json.dump(data, file, indent=4)
            print("matches set successfully.")         