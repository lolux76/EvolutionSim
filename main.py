import random
import sys
import pygame
import time

from src.carnivorous import *
from src.food import *

# Initialisation
pygame.init()

width, height = 800, 600
black = 0, 0, 0  # Black is for background
white = 255, 255, 255  # White is for big winter event
yellow = 255, 255, 0  # Yellow is for big summer event
red = 255, 0, 0  # Carnivorous color
brown = 90, 40, 0  # Meat color
green = 0, 255, 0  # Vegetables color
blue = 0, 0, 255  # Herbivorous color

# Creating screen
screen = pygame.display.set_mode((width, height))

# Alive entities, null by starting the simulation
activeAnimals = []
activeFood = []

# Title
pygame.display.set_caption("Evolution Simulation")


# Drawing animals function:
def drawing_animals():
    for animal in activeAnimals:
        if animal.isCarnivorous:
            animal_color = red  # carnivorous will all be red
        else:
            animal_color = blue  # herbivorous will all be blue
        pygame.draw.circle(screen, animal_color, (animal.positionX, animal.positionY),
                           animal.weight)


def drawing_food():
    for food in activeFood:
        if food.__class__ == basic_meet:
            food_color = brown  # meat will all be brown
        else:
            food_color = green  # vegetables will all be green
        pygame.draw.circle(screen, food_color, (food.positionX, food.positionY),
                           food.size)


# Simulation loop
begin = True
running = True
simSpeed = 5  # Speed of the simulation (in FPS)
randomMovementDirectionChangeTimer = random.randint(20, 30)
timeToSpawnFood = 4
fpsCounter = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background color
    screen.fill(black)

    # Spawn food
    if fpsCounter % timeToSpawnFood == 0:
        for i in range(10):
            activeFood.append(basic_meet(random.randint(50, width - 50), random.randint(50, height - 50)))

    # Updating food
    for food in activeFood:
        if food.quantity == 0:
            activeFood.remove(food)

    # Change animals movement direction
    if fpsCounter % randomMovementDirectionChangeTimer == 0:
        for current_animal in activeAnimals:
            current_animal.changeDirection()

        randomMovementDirectionChangeTimer = random.randint(20, 30)  # Calculating new random direction change timer

    for current_animal in activeAnimals:
        activeAnimals = current_animal.action(width, height, activeAnimals, activeFood)

    # Drawing on the screen
    drawing_food()
    drawing_animals()

    pygame.display.update()
    fpsCounter += 1
    clock.tick(simSpeed + 20)

    # Stats in console
    if fpsCounter % 100 == 0:
        print(len(activeAnimals))

    # Initialisation of the sim
    if begin:
        while len(activeAnimals) < 30:
            activeAnimals.append(carnivorous(random.randint(55, width - 55), random.randint(55, height - 55)))
            activeAnimals.append(carnivorous(random.randint(55, width - 55), random.randint(55, height - 55), gender=1))
        begin = False

if __name__ == '__main__':
    print("Hello World")
