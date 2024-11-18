import random
from ability import Ability
from armor import Armor


class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armor = list()
        
        
    
    #Fight method 
    def fight (self,opponent):
        self.opponent = opponent
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        #1) randomly choose winner,
        # Hint: Look into random library, more specifically the choice method
        winner = random.choice([self,opponent])
        print(f"{winner.name} is the winner of this match." )
        
        #Strech Goal for Fight Method
        
        # chance = self.starting_health + opponent.starting_health
        # percentage1 = self.starting_health/chance
        # percentage2 = opponent.starting_health/chance

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage +=ability.attack()
        return total_damage
        
        
        
        
        
        
if __name__ =="__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
