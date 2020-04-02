

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


class BaseballTeam():
    def __init__(self, name, city, starting_pitcher, players=["Player 1"]):
        self.name = name
        self.city = city
        self.players = players
        self.starting_pitcher = starting_pitcher

    def advertise(self):
        print(f"HEY COME TO {self.city.upper()} TO SEE OUR GAMES!!!")

    @property
    def full_name(self):
        return f"{self.city} {self.name}"


if __name__ == "__main__":

    football_team = Team("Cowboys", "Dallas")
    print(football_team.full_name)
    football_team.advertise()

    teams = [
        {"city": "New York", "name": "Yankees", "pitcher": "Cassidy"},
        {"city": "New York", "name": "Mets", "pitcher": "Angelica"},
        {"city": "Boston", "name": "Red Sox", "pitcher": "Dom"},
        {"city": "New Haven", "name": "Ravens", "pitcher": "Aspen"},
        {"city": "Washington", "name": "Nationals", "pitcher": "Michelle"}
    ]

    for team_attributes in teams:
        team = BaseballTeam(name=team_attributes["name"], city=team_attributes["city"],
                            starting_pitcher=team_attributes["pitcher"])
        print("-------")
        print(team.city)
        print(team.full_name)
        print(team.players)
        print(team.starting_pitcher)
        team.advertise()
