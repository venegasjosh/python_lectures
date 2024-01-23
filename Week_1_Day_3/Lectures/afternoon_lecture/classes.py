import random


class Character:
  all_characters = []
  def __init__(self, name, health = 30, power = 8, armor=8, speed=8):
    self.name = name
    self.health = health
    self.power = power
    self.armor = armor
    self.speed = speed
    Character.all_characters.append(self)
    
    #method to gain or lose health
    def gain_health(self, amount):
      self.health += amount
      #return self so we can chain methods in the future
      return self
    
    def lose_health(self, amount):
      self.health -= amount
      return self
    
    #method for attacking
    
    def attack(self, target):
      
    
    # method for blocking
    
c1 = Character("Tyler")
c2 = Character("Josh")


print(Character.all_characters)