from weapon import Weapon

class Robot:

    def __init__(self):
        self.name = "R2D2"
        self.health = 100
        self.active_weapon = Weapon()

    def attack(self, dinosaur):
        dinosaur -= self.active_weapon.attack_power



# current_attack = self.active_weapon
# dinosaur -= current_attack.attack_power