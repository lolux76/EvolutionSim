import random

from src.animals import animal
from src.food import *
import math


class carnivorous(animal):
    isCarnivorous = True
    aggresivity = 0

    # Constructor
    def __init__(self, positionX, positionY, health=100, weight=5, speed=5, energy=5, hunger=50, strength=5, gender=0):
        self.positionY = positionY
        self.positionX = positionX
        self.health = health
        self.weight = weight
        self.speed = speed / weight
        self.energy = energy
        self.hunger = hunger
        self.strength = strength
        self.gender = gender

        # Random mutation
        if random.randint(1, 100) == 1:
            self.weight = random.randint(1, 10)

    def canReproduce(self, animal):
        if self != animal and animal.__class__ == carnivorous:  # Isn't reproducing with itself and animal is a carnivorous
            if self.gender != animal.gender:
                if self.fertility == 100 and animal.fertility == 100:
                    minWeight = self.weight if self.weight < animal.weight else animal.weight
                    if math.sqrt(math.pow(self.positionX - animal.positionX, 2) + math.pow(self.positionY - animal.positionY, 2)) \
                            <= minWeight + 10:
                        return True
        return False

    def reproduction(self, activeAnimals):
        for animal in activeAnimals:
            if self.canReproduce(animal):
                animal.fertility = 0
                self.fertility = 0
                newWeigth = (self.weight + animal.weight) / 2
                activeAnimals.append(carnivorous(self.positionX, self.positionY, weight=newWeigth, gender=random.randint(0, 1)))
                break
        return activeAnimals

    def canEat(self, food):
        if food.__class__ == basic_meet:
            minSize = self.weight if self.weight < food.size else food.size
            if math.sqrt(
                    math.pow(self.positionX - food.positionX, 2) + math.pow(self.positionY - food.positionY, 2)) \
                    <= minSize + 10:
                return True
        return False

    def heat(self, activeFood):
        if self.hunger < 100:
            for food in activeFood:
                if self.canEat(food):
                    self.hunger = food.quantity
                    food.quantity = 0
                    if self.hunger > 100:
                        self.hunger = 100


    def action(self, maxWidth, maxHeight, activeAnimals, activeFood):
        activeAnimals = super().action(maxWidth, maxHeight, activeAnimals, activeFood)
        self.heat(activeFood)
        activeAnimals = self.reproduction(activeAnimals)
        return activeAnimals

    def toString(self):
        super(carnivorous, self).toString()
        print("is Carnivorous : ", self.isCarnivorous)
        print("Agressivity ; ", self.aggresivity)
