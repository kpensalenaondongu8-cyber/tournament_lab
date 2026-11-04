from tournament.register_team import register_team
from tournament.list_teams import list_teams
from tournament.assign_matches import generate_tournament_fixture
from tournament.list_fixtures import list_fixtures
from tournament.record_result import record_result
from tournament.status import update_match_status
from tournament.standings import display_standings


print("-"*4, "MENU", "-"*4)
print("1.Register team\n2.list teams\n3.generate schedule\n4.list fixtures\n5.record results\n6.update_status\n7.standings\n8.show champion\n0.quit")
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

elif user_input == "5":
    user_input1 = input("Enter match_id: ")
    try:
       user_input2 = int(input("Enter home score: "))
       user_input3 = int(input("Enter away score: "))
       record_result(user_input1, user_input2, user_input3)    
    except ValueError:
        print("Score can only be an integer.")   

elif user_input == "6":
     user_input1 = input("Enter match_id: ")
     user_input2 = input("Enter status: ")
     update_match_status(user_input1, user_input2)

elif user_input == "7":
    print("\n--- LEAGUE STANDINGS ---")
    print(display_standings())