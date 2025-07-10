class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Coach(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

class Player(Person):
    def __init__(self, name, age, position, number):
        if age > 23:
            print(f"Warning: {name} is over 23!")
        super().__init__(name, age)
        self.position = position
        self.number = number

class Staff(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

class Team:
    def __init__(self, name):
        self.name = name
        self.head_coach = None
        self.assistant_coach = None
        self.players = []
        self.staffs = []

    def set_head_coach(self, coach):
        if coach.role.lower() == "head coach":
            self.head_coach = coach
        else:
            print("Error: Wrong role for head coach")

    def set_assistant_coach(self, coach):
        if coach.role.lower() == "assistant coach":
            self.assistant_coach = coach
        else:
            print("Error: Wrong role for assistant coach")

    def add_player(self, player):
        if len(self.players) < 15:
            self.players.append(player)
        else:
            print("Player limit reached (15)")

    def add_staff(self, staff):
        self.staffs.append(staff)

    def show_team(self):
        print("== TEAM INFO ==")
        print("Team Name:", self.name)
        print("Head Coach:", self.head_coach.name if self.head_coach else "None")
        print("Assistant Coach:", self.assistant_coach.name if self.assistant_coach else "None")
        print("\nPlayers:")
        for p in self.players:
            print(f"#{p.number} {p.name} ({p.position}) - age {p.age}")
        print("\nStaff:")
        for s in self.staffs:
            print(f"{s.name} - {s.job}")


# === contoh penggunaan ===
if __name__ == "__main__":
    team = Team("FC Cakrawala Muda")

    team.set_head_coach(Coach("Budi", 44, "Head Coach"))
    team.set_assistant_coach(Coach("Agus", 39, "Assistant Coach"))

    for i in range(1, 16):
        team.add_player(Player("Pemain " + str(i), 20 + (i % 4), "Midfield", i))

    team.add_staff(Staff("Siti", 29, "Medis"))
    team.add_staff(Staff("Andi", 35, "Manajer"))

    team.show_team()
