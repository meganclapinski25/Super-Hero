from ability import Ability
from armor import Armor
import random

class Weapon(Ability):
    def attack(self):
        random_ability = random.randint(self.max_damage // 2, self.max_damage)
        return random_ability  
    
if __name__ == "__main__":
    print("hello")