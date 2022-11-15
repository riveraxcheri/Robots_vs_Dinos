from weapon import Weapon

class Robot:

    def __init__(self):
        self.name = "R2D2"
        self.health = 100
        self.active_weapon = Weapon()
        pass

    def attack(self, dinosaur:int):
        while self.health > 0:
            dinosaur -= self.active_weapon.attack_power
            if self.attack:
                print (f"R2D2 attacked dealing {self.active_weapon.attack_power} damage! \n Rex health is now {dinosaur}")
                return
            else:
                return