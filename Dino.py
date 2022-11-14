class Dinosaur:

    def __init__(self):
        self.name = "Rex"
        self.health = 100
        self.attack_power = 50

    def attack(self, robot):
        robot -= self.attack_power