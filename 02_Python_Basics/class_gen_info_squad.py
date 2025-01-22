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

    def add_member(self):
        add_hero = input("Möchtest du einen neuen Helden zu diesem Squad hinzufügen? (ja/nein): ").lower()
        
        if add_hero == 'ja':
            name = input("Name des Helden: ")
            age = int(input("Alter des Helden: "))
            secret_identity = input("Geheimidentität des Helden: ")
            
            powers_input = input("Kräfte des Helden (durch Kommas getrennt): ")
            powers = [power.strip() for power in powers_input.split(",")]

            new_member = Member(
                name=name,
                age=age,
                secret_identity=secret_identity,
                powers=powers
            )
            self.members.append(new_member)
            
            print(f"\n{new_member.name} wurde erfolgreich zum Team {self.squad_name} hinzugefügt!")
        else:
            print("Kein neuer Held wurde hinzugefügt. Weiter zum nächsten Squad.")

    def remove_hero(self):
        print("\nAktuelle Mitglieder:")
        for i, member in enumerate(self.members):
            print(f"{i + 1}. {member.name}")
        
        delete_hero = input("Möchtest du einen Helden aus diesem Squad löschen? (ja/nein): ").lower()
        
        if delete_hero == 'ja':
            try:
                hero_to_remove = int(input("Gib die Nummer des Helden ein, den du löschen möchtest: ")) - 1

                if 0 <= hero_to_remove < len(self.members):
                    removed_hero = self.members.pop(hero_to_remove)
                    print(f"\n{removed_hero.name} wurde erfolgreich aus dem Squad entfernt.")
                else:
                    print("Ungültige Nummer, bitte versuche es erneut.")
            except ValueError:
                print("Bitte gib eine gültige Nummer ein.")
        else:
            print("Kein Held wurde gelöscht. Weiter zum nächsten Squad.")

    def print_squad_data(self):
        print("\nSquad Details: \n")
        print(f"Squad Name: \t \t \t{self.squad_name}")
        print(f"Home Town: \t \t \t{self.home_town}")
        print(f"Formed: \t \t \t{self.formed}")
        print(f"Status: \t \t \t{self.status}")
        print(f"Active: \t \t \t{self.active}")
        
        print("\nZu Diesem Squad Gehören Folgende Superhelden:")
        
        print("-------------------------------------------------------------------------------------------------------")
        print("\nMember Details:")
        
        for member in self.members:
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

    squad.print_squad_data()
    squad.add_member()
    squad.remove_hero()
