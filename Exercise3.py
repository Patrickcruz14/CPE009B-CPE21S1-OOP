class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive values.")
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle: Length = {self.length}, Width = {self.width}"

try:
    rect = Rectangle(5, 3)
    print(rect)
    print("Perimeter:", rect.Perimeter())
    print("Area:", rect.Area())
except ValueError as e:
    print(e)
  
