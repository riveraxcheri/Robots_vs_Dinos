from Dino import Dinosaur
from Robot import Robot

class Battlefield:
    
    def __init__(self):
        self.robot_one = Robot()
        self.dino_one = Dinosaur()
        pass

    def display_welcome(self):
        self.welcome = "\nWelcome to the Battlefield!\nOnly one can win!"
        print(self.welcome)
        pass

    def battle_phase(self):
        dino_hp = self.dino_one.health
        robot_hp = self.robot_one.health
        self.robot_one.health = self.dino_one.attack(robot_hp)
        self.dino_one.health = self.robot_one.attack(dino_hp)
        if self.robot_one.health <= 0 and self.dino_one.health <= 0:
            self.display_winner()
        else:
            self.battle_phase()

    def display_winner(self):
        if self.dino_one.health > 0:
            print (f"{self.dino_one.name} Wins!")
        elif self.robot_one.health > 0:
            print (f"{self.robot_one.name} Wins!")
        return
        

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass
