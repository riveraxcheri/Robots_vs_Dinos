from Dino import Dinosaur
from Robot import Robot

class Battlefield:
    
    def __init__(self):
        self.robot_one = Robot()
        self.dino_one = Dinosaur()

    def display_welcome(self):
        print("\nWelcome to the Battlefield!\nOnly one can win!")

    def battle_phase(self):
        self.dino_one.attack(self.robot_one.health)
        # self.robot_one.health -= self.dino_one.attack_power
        # self.dino_one.health -= self.robot_one.active_weapon.attack_power
        if self.robot_one.health <= 0 and self.dino_one.health <= 0:
            pass

    def display_winner(self):
        while self.robot_one.health > 0 and self.dino_one.health > 0:
            print (f"{self.robot_one.name} Wins!")
            print (f"{self.dino_one.name} Wins!")

    def run_game(self):
        self.display_welcome
        self.battle_phase
        self.display_winner