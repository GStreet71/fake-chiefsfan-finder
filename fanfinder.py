import os

players = [
    {"name": "Patrick Mahomes", "draft": 2017, "college": ["Texas Tech", "TTU"], "jersey": 15},
    {"name": "Travis Kelce", "draft": 2013, "college": ["Cincinatti", "UC"], "jersey": 87},
    {"name": "Chris Jones", "draft": 2016, "college": ["Mississippi State", "MSU"], "jersey": 95},
    {"name": "Isiah Pacheco", "draft": 2022, "college": ["Rutgers", "RU"], "jersey": 10},
    {"name": "Rashee Rice", "draft": 2023, "college": ["Southern Methodist University", "SMU"], "jersey": 4},
    {"name": "Trent Mcduffie", "draft": 2022, "college": ["Washington", "WU"], "jersey": 22},
    {"name": "Xavier Worthy", "draft": 2024, "college": ["Texas", "UT"], "jersey": 1},
    {"name": "Harrison Butker", "draft": 2017, "college": ["Georgia Tech", "GT"], "jersey": 7},
    {"name": "Nick Bolton", "draft": 2021, "college": ["Missouri", "MU"], "jersey": 32},
    {"name": "Justin Reid", "draft": 2018, "college": ["Stanford"], "jersey": 20},
    {"name": "Creed Humphries", "draft": 2021, "college": ["Oklahoma", "OU"], "jersey": 52},
    {"name": "George Karlaftis", "draft": 2022, "college": ["Purdue", "PU"], "jersey": 52},
    {"name": "Joe Thuney", "draft": 2021, "college": ["Oklahoma", "OU"], "jersey": 52},
    {"name": "Kareem Hunt", "draft": 2017, "college": ["Toledo", "TU"], "jersey": 27},
    {"name": "Carson Steele", "draft": "undrafted", "college": ["Ball State", "BSU"], "jersey": 42}
]

os.system("clear")
print("\N{american football} Fake Chiefs Fan Finder \N{eyes}")
print("----------------------------------\n")

def validate_name():
    while True:
        choice = input("Who is your favorite Chiefs player?: ").capitalize()
        
        for player in players:
            split_name = player["name"].split()
            match = any(part.capitalize() in choice for part in split_name)
            if match:
                validate_jersey(player)
                return player
        print(f"{choice} not found. Try again\n")

def validate_jersey(player):
    choice = input(f"\nOh really?! Well what's {player['name']}'s jersey number then?: ")

    if  choice.isdigit():
        if int(choice) == player["jersey"]:
            validate_college(player)
            return player
        else:
            print(f"Wrong. {choice} is not {player['name']}'s jersey neumber. See! FAKE Cheifs fan!\n")
    else:
        print("Invalid response. Enter a valid jersey number.\n")    

def validate_college(player):
    choice = input(f"\nYou got that by pure luck. Okay then, what college did {player['name']} attend?: ").capitalize()
    choice_lower = choice.lower()    
    colleges = player['college']
    colleges_lower = [college.lower() for college in colleges]
    
    for college in colleges_lower:
        if choice_lower in colleges_lower:
            validate_draft(player)
            return
        
    print(f"Wrong college for {player['name']}. See! FAKE Chiefs fan!\n")

def validate_draft(player):
    choice = input(f"\nHmph! Those were easy, last one. What year was {player['name']} drafted?: ").capitalize()
    
    if  choice.isdigit():
        if int(choice) == player["draft"]:
            print("\n*******************************************************************")
            print("\n  Okay! You are a real Chiefs fan. - WELCOME TO CHIEFS KINGDOM!!!\n")
            print("*******************************************************************")       
        else:
            print(f"The {choice} draft was not {player['name']}'s draft year. See! FAKE Chiefs fan!\n")
    else:
        print("Invalid response. Enter a valid draft year.\n")    
    
def main():
    validate_name()

if __name__ == '__main__':
    main()