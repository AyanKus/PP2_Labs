from math import pow, sqrt

class Point:

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def show(self):
        print(f"x = {self.x}, y = {self.y}") 

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

    def dist(self, p2):
        return sqrt(pow(self.x - p2.x, 2) + pow(self.y - p2.y, 2))