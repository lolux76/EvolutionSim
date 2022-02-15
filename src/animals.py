import random


class animal:
    # Position
    positionX = 0
    positionY = 0

    # Stats
    health = 0  # If reduced to 0, animal is dead
    weight = 0  # Weight will be used to define the size of the animal
    speed = 0  # Move speed of the animal
    energy = 0  # Animal capacity to attack, if reduced to 0, animal will need some time to recover until it can fight more
    hunger = 0  # Animal current hunger, if falling to 0 this animal will start to take damages
    strength = 0  # Ability to fight against others animals
    fertility = 100
    gender = 0

    # Movement attributes
    directionX = 0
    directionY = 0

    def changeDirection(self):  # Change the current direction to random direction
        self.directionX = random.randint(0, 1)
        self.directionY = random.randint(0, 1)

    def move(self, maxWidth, maxHeight):
        # If we are on a boundary, changing the direction to avoid leaving the screen
        if self.positionX + self.weight >= maxWidth - 50:
            self.directionX = 0
        if self.positionY + self.weight >= maxHeight - 50:
            self.directionY = 0

        if self.positionX - self.weight <= 50:
            self.directionX = 1
        if self.positionY - self.weight <= 50:
            self.directionY = 1

        # Moving
        if self.directionX == 1:
            self.positionX += self.speed
        else:
            self.positionX -= self.speed

        if self.directionY == 1:
            self.positionY += self.speed
        else:
            self.positionY -= self.speed

    def action(self, maxWidth, maxHeight, activeAnimals, activeFood):
        # Updating stats
        if self.fertility < 100:
            self.fertility += 1

        if self.hunger != 0:
            self.hunger -= self.weight / 10
            if self.health != 100:
                self.health += 1
        else:
            self.health -= 1
        if self.hunger < 0:  # Min hunger is 0
            self.hunger = 0

        self.move(maxWidth, maxHeight)

        # If health = 0, animal is dead
        if self.health == 0:
            activeAnimals.remove(self)

        return activeAnimals

    def toString(self):
        print("Health : ", self.health)
        print("Weight : ", self.weight)
        print("Speed : ", self.speed)
        print("Energy : ", self.energy)
        print("Hunger : ", self.energy)
        print("Defence : ", self.energy)
        print("Sexe : ", self.gender)
