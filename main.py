from tournament.register_team import register_team
from tournament.list_teams import list_teams
from tournament.assign_matches import generate_tournament_fixture
from tournament.list_fixtures import list_fixtures


print("-"*4, "MENU", "-"*4)
print("1.Register team\n2.list teams\n3.generate schedule\n4.list fixtures\n5.record results\n6.standings\n7.show champion\n0.quit")
user_input = input("Select from the menu: ")
if user_input == "1":
    user_input1 = input("Enter team name: ")
    retsult = register_team(user_input1)
    print(retsult)

elif user_input == "2":
    list_teams()
    
elif user_input == "3":
    generate_tournament_fixture()

elif user_input  == "4":
    list_fixtures() 