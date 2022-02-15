class food:
    positionX = 0
    positionY = 0
    quantity = 0
    size = 5


class basic_meet(food):
    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY
        self.quantity = 50


class basic_vegetable:
    quantity = 5
