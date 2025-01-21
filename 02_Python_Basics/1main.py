import json
from class_gen_info_member import Member
from class_gen_info_squad import add_member, Squad, remove_hero, print_squad_data

# Load JSON data from a file
with open('Hero.json', 'r') as file:
    json_hero = json.load(file)

# Loop through each squad in the JSON data
for squad_data in json_hero:
    members = []
    for member in squad_data['members']:
        name = member["name"]
        age = member["age"]
        secret_identity = member["secretIdentity"]
        powers = member["powers"]
        members.append(Member(name, age, secret_identity, powers))
    
    squad = Squad(
        squad_name=squad_data['squadName'],
        home_town=squad_data['homeTown'],
        formed=squad_data['formed'],
        status=squad_data['status'],
        secret_base=squad_data['secretBase'],
        active=squad_data['active'],
        members=members
    )

    # Use the Squad object
    print_squad_data(squad)
    add_member(squad)
    remove_hero(squad)