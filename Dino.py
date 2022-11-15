class Dinosaur:

    def __init__(self):
        self.name = "Rex"
        self.health = 100
        self.attack_power = 50
        pass

    def attack(self, robot:int):
        while self.health > 0:
            robot -= self.attack_power
            if self.attack:
                print (f"Rex attacked dealing {self.attack_power} damage! \n R2D2 health is now {robot}")
                return
            else:
                return