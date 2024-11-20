import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        
        
    
    #Fight method 
    def fight (self,opponent):
        
        if not self.abilities and not opponent.abilities:
            return ("Draw")

        while self.is_alive() and opponent.is_alive():
            opponent_damage = self.attack()
            self_damage = opponent.attack()
            
            opponent.take_damage(opponent_damage)
            self.take_damage(self_damage)
        
       
        if self.is_alive():
            print(f"{self.name} won!")
        elif opponent.is_alive():
            print(f"{opponent.name} won!")

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
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        
if __name__ =="__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
