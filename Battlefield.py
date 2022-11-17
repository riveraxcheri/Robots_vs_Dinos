from Dino import Dinosaur
from Robot import Robot

class Battlefield:
    
    def __init__(self):
        self.robot_one = Robot("R2D2", 100)
        self.dino_one = Dinosaur("Rex", 100, 50)
        pass

    def display_welcome(self):
        self.welcome = "\nWelcome to the Battlefield!\nOnly one can win!"
        print(self.welcome)
        pass

    def battle_phase(self):
        self.dino_one.attack(self.robot_one.health)
        defeat = False
        while defeat == False:
            if self.dino_one.health > 0:
                self.robot_one.health -= self.dino_one.attack_power
                print (f"Rex attacked dealing {self.dino_one.attack_power} damage! \n R2D2 health is now {self.robot_one.health}")
                self.robot_one.attack(self.dino_one.health)
            elif self.dino_one.health <= 0:
                defeat = True
                return self.display_winner()
            if self.robot_one.health > 0:
                self.dino_one.health -= self.robot_one.active_weapon.attack_power
                print (f"R2D2 attacked dealing {self.robot_one.active_weapon.attack_power} damage! \n Rex health is now {self.dino_one.health}")
            elif self.robot_one.health <= 0:
                defeat = True    
        else:
            defeat = True
            return self.display_winner()

    def display_winner(self):
        if self.dino_one.health >= 0:
            print (f"{self.dino_one.name} Wins!")
        elif self.robot_one.health >= 0:
            print (f"{self.robot_one.name} Wins!")
        return
        

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        pass
