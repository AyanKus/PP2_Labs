class Shape:

    def area(self):
        return 0
    
class Square(Shape):

    def __init__(self, length: int):
        self.length = length
    
    def area(self):
        return self.length * self.length