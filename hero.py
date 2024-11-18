import random

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    
    #Fight method 
    def fight (self,opponent):
        self.opponent = opponent
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        #1) randomly choose winner,
        # Hint: Look into random library, more specifically the choice method
        winner = random.choice([self,opponent])
        print(f"{winner.name} is the winner of this match." )
        
        
        
        
        
        
        
if __name__ =="__main__":
    my_hero = Hero ("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)