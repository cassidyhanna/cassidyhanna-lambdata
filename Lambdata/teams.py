

# example teams.py (functional approach)

class Team():
    def __init__(self, name, city):
        self.name = name
        self.city = city


def advertise(my_team):
    print(f"HEY COME TO {my_team['city'].upper()} TO SEE OUR GAMES!!!")


def full_name(my_team):
    return f"{my_team['city']} {my_team['name']}"


if __name__ == "__main__":
    '''teams = [
        {"city": "New York", "name": "Yankees"},
        {"city": "New York", "name": "Mets"},
        {"city": "Boston", "name": "Red Sox"},
        {"city": "New Haven", "name": "Ravens"},
        {"city": "Washington", "name": "Nationals"}
    ]

    for team in teams:
        print("-------")
        print(full_name(team))
        advertise(team)
    '''
    # initialize / create an instance of the object
    team = Team(city="Washington", name="Wizards")
    print(team)
    print(type(team))
    # invoking attributes
    print(team.name)
    # invoking attributes
    print(team.city)

    # initialize / create an instance of the object
    team2 = Team("Giants", "New York")
    print(type(team2))
    # invoking attributes
    print(team2.name)
    # invoking attributes
    print(team2.city)
