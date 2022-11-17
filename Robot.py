from weapon import Weapon

class Robot:

    def __init__(self, name, hp:int):
        self.name = name
        self.health = hp
        self.active_weapon = Weapon("Laser", 50)
        pass

    def attack(self, dinosaur:int):
        pass