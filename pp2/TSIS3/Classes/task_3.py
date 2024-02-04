from task_2 import Shape

class Rectangle(Shape):

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    