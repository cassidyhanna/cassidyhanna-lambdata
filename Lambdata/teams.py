

# example teams.py ( OOP approach)

class Team():
    def __init__(self, name, city="CITY NAME", players=["Player 1"]):
        self.name = name
        self.city = city
        self.players = players

    def advertise(self):
        print(f"HEY COME TO {self.city.upper()} TO SEE OUR GAMES!!!")

    @property
    def full_name(self):
        return f"{self.city} {self.name}"


if __name__ == "__main__":
    teams = [
        {"city": "New York", "name": "Yankees"},
        {"city": "New York", "name": "Mets"},
        {"city": "Boston", "name": "Red Sox"},
        {"city": "New Haven", "name": "Ravens"},
        {"city": "Washington", "name": "Nationals"}
    ]

    for team_attributes in teams:
        team = Team(name=team_attributes["name"], city=team_attributes["city"])
        print("-------")
        print(team.city)
        print(team.full_name)
        print(team.players)
        team.advertise()
