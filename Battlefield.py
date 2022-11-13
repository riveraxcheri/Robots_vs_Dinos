from Dino import Dinosaur
from Robot import Robot

class Battlefield:

    def __init__(self):
        self.run_game(self)

    def run_game(self):
        self.display_welcome(self)
        self.battle_phase(self)
        self.display_winner(self)

    def display_welcome(self):
        self.welcome= print("\nWelcome to the Battlefield!\nOnly one can win!")

    def battle_phase(self):
        self.phase_one = Dinosaur.attack(Robot.health)
        print(self.phase_one)
        self.phase_two = Robot.attack(Dinosaur.health)
        print(self.phase_two)

    def display_winner(self):
        self.winner= print("")

