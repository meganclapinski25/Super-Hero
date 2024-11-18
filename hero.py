import random
from ability import Ability
from armor import Armor


class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        
        
    
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

    #Add and Attack with Ability 
    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage +=ability.attack()
        return total_damage
        
    #Add and Defend with Armor
    def add_armor(self,armor):
        self.armors.append(armor)    
        
    def defend(self):
        total_block = 0
        for armor in self.armors:
            if self.current_health == 0:
                print(f"The hero is currently dead and cannot defend")
            elif self.armors == 0:
                print(f"The hero has no armor there cannot defend")
            else:
                total_block += armor.block()
        return total_block
    
    #Take Damage Method
    def take_damage(self, damage):
        defense = self.defend()
        temp = damage - defense
        self.current_health -=temp      
      
    #Is Alive Method 
    def is_alive(self):
        if self.current_health <=0 :
            return False
        elif self.current_health >0:
            return True  
        
        
if __name__ =="__main__":
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
