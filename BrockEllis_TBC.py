# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:17:10 2024

@author: uball
"""

import random
    
class Character(object):
    def __init__(self):
        self.name = "anonymous"
        self.hitPoints = 20
        self.hitChance = 50
        self.maxDamage = 5
        self.armor = 1
        
        
    @property 
    def name(self):
        return self.__name
           
    @name.setter
    def name(self, value):
        self.__name = value 
        
    @property
    def hitPoints(self):
        return self.__hitPoints
        
    @hitPoints.setter
    def hitPoints(self, value):
        value = self.testInt(value, 0, 1000, 0)
        self.__hitPoints = value
        
    @property
    def hitChance(self):
        return self.__hitChance
        
    @hitChance.setter
    def hitChance(self, value):
        value = self.testInt(value, 0, 100, 0)
        self.__hitChance = value
            
    @property
    def maxDamage(self):
        return self.__maxDamage
       
    @maxDamage.setter
    def maxDamage(self, value):
        value = self.testInt(value, 0, 10, 0)
        self.__maxDamage = value
        
    @property
    def armor(self):
        return self.__armor
        
    @armor.setter
    def armor(self, value):
        value = self.testInt(value, 0, 10, 0)
        self.__armor = value   
            
            
    def testInt(self, value, min = 0, max = 100, default = 0):
        out = default
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")
            
        return out
       
    
    def hit(self, enemy):
        """ fights one round with another character """
        if random.randint(1, 100) < self.hitChance: 
            print(f"{self.name} hits {enemy.name}...")
            damage = random.randint(1, self.maxDamage)
            print(f" for {damage} points of damage...")
            damage -= enemy.armor
            if damage < 0:
                damage = 0
            if enemy.armor > 0:
                print(f" but {enemy.name}'s armor absorbs {enemy.armor} points")
            enemy.hitPoints -= damage
        else: 
            print(f"{self.name} misses {enemy.name}")
        
    def printStats(self):
        print(f"""
{self.name}
    Hit Points: {self.hitPoints}
    Hit Chance: {self.hitChance}
    Max Damage: {self.maxDamage}
    Armor: {self.armor}
    """)
    
def basicFight(player1, player2):
    """ performs a fight until a player's hp is empty """
    
    keepGoing = True
    while keepGoing: 
        player1.hit(player2)
        player2.hit(player1)
        
        print(f"{player1.name} HP: {player1.hitPoints}")
        print(f"{player2.name} HP: {player2.hitPoints}")
        print() 
        
def userFight(player, enemy):
    """ modify the fight function to allow some choices """
    keepGoing = True
    while keepGoing:
        
        print("""
           1) fight
           2) heal
           3) rest """)
        userChoice = input("What will you do?")
        if userChoice == "1":
            player.hit(enemy)
        elif userChoice == "2":
            print("You feel healthier")
            player.hitPoints += 5
        elif userChoice == "3":
            print("You feel yourself getting stronger")
            player.maxDamage += 2 
        else: 
            print("Invalid choice. Try again.")
            continue
            
        enemy.hit(player)
        print(f"{player.name} HP: {player.hitPoints}")
        print(f"{enemy.name} HP: {enemy.hitPoints}")
        print() 
            
            
def main():
    player = Character()
    player.name = "Hero"
    player.hitPoints = 20
    player.hitChance = 50
    player.maxDamage = 5
    player.armor = 1
    player.printStats()
    
    enemy = Character()
    enemy.name = "Monster"
    enemy.hitPoints = 30
    enemy.hitChance = 35
    enemy.maxDamage = 6
    enemy.armor = 0
    enemy.printStats()
    
    # Basic fight
    # basicFight(player, enemy)
    
    # User controlled fight
    userFight(player, enemy)

if __name__ == "__main__":
    main()