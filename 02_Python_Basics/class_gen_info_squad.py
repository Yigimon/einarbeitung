import json
from class_gen_info_member import Member

#! Klasse Squad
class Squad:
    def __init__(self, squad_name: str, home_town: str, formed: int, status: str, secret_base: bool, active: int, members: list[Member]):
      self.squad_name = squad_name
      self.home_town = home_town
      self.formed = formed
      self.status = status
      self.secret_base= secret_base
      self.active = active
      self.members = members
      
    def __repr__(self):
       return f"Squad(squad_name={self.squad_name}, home_town={self.home_town}, formed={self.formed}, status={self.status}, secret_base={self.secret_base}, active={self.active}, members={self.members})"

print(Squad)

#! Funktion zum hinzufügen einen neuen Helden zu Members
def add_member(squad):
    add_hero = input("Möchtest du einen neuen Helden zu diesem Squad hinzufügen? (ja/nein): ").lower()
    
    if add_hero == 'ja':
        # Benutzereingabe für den neuen Helden
        name = input("Name des Helden: ")
        age = int(input("Alter des Helden: "))
        secret_identity = input("Geheimidentität des Helden: ")
        
        # Kräfte hinzufügen
        powers_input = input("Kräfte des Helden (durch Kommas getrennt): ")
        powers = [power.strip() for power in powers_input.split(",")]

        # Erstelle ein neues Member-Objekt
        new_member = Member(
            name=name,
            age=age,
            secret_identity=secret_identity,
            powers=powers
        )
        # Fügt den Helden zur Liste hinzu
        squad.members.append(new_member)
        
        # Gibt den hinzugefügten Helden aus
        print(f"\n{new_member.name} wurde erfolgreich zum Team {squad.squad_name} hinzugefügt!")
    
    else:
        print("Kein neuer Held wurde hinzugefügt. Weiter zum nächsten Squad.")


#! Funktion zum entfernen eines Helden aus Members
def remove_hero(squad):
    # Ausgabe der aktuellen Mitglieder
    print("\nAktuelle Mitglieder:")
    for i, member in enumerate(squad.members):
        print(f"{i + 1}. {member.name}")
    
    delete_hero= input("Möchtest du einen  Helden aus diesem Squad löschen? (ja/nein): ").lower()
    
    if delete_hero == 'ja':

        # Abfrage, welchen Helden der Benutzer löschen möchte
        try:
            hero_to_remove = int(input("Gib die Nummer des Helden ein, den du löschen möchtest: ")) - 1

            if 0 <= hero_to_remove < len(squad.members):
                removed_hero = squad.members.pop(hero_to_remove)
                print(f"\n{removed_hero.name} wurde erfolgreich aus dem Squad entfernt.")
            else:
                print("Ungültige Nummer, bitte versuche es erneut.")
        except ValueError:
            print("Bitte gib eine gültige Nummer ein.")

    else:
        print("Kein Held wurde gelöscht. Weiter zum nächsten Squad.")

#! Funktion zum ausgeben der Squad Daten
def print_squad_data(squad):
    print("\nSquad Details: \n")
    print(f"Squad Name: \t \t \t{squad.squad_name}")
    print(f"Home Town: \t \t \t{squad.home_town}")
    print(f"Formed: \t \t \t{squad.formed}")
    print(f"Status: \t \t \t{squad.status}")
    print(f"Active: \t \t \t{squad.active}")
    
    print("\nZu Diesem Squad Gehören Folgende Superhelden:")
    
    # Mitglieder ausgeben
    print("-------------------------------------------------------------------------------------------------------")
    print("\nMember Details:")
    
    for member in squad.members:
      print(f"Name: \t \t \t \t{member.name}")
      print(f"Secret Identity: \t \t{member.secret_identity}")
      print(f"Age: \t \t \t \t{member.age}")
      print(f"Powers: \t \t \t{', '.join(member.powers)}")
      print("-------------------------------------------------------------------------------------------------------")

# JSON-Datei wird ausgelesen und an die Funktionen übergeben
with open('Hero.json', 'r') as file:
    json_hero = json.load(file)

# Funktionen aufrufen
for squad_data in json_hero:
    members = []
    for member_data in squad_data["members"]:
        member = Member(
            name=member_data["name"],
            age=member_data["age"],
            secret_identity=member_data["secretIdentity"],
            powers=member_data["powers"]
        )
        members.append(member)

    squad = Squad(
        squad_name=squad_data["squadName"],  
        home_town=squad_data["homeTown"],
        formed=squad_data["formed"],
        status=squad_data["status"],
        secret_base=squad_data["secretBase"],
        active=squad_data["active"],
        members=members
    )

    print_squad_data(squad)
    add_member(squad)
    remove_hero(squad)
