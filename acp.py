import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius  
    
    def area(self):
        return math.pi * (self.radius ** 2)

def create_circle():
    radius = float(input("Enter the radius of the circle: "))
    circle_obj = Circle(radius)
    print("Perimeter:", circle_obj.perimeter())
    print("Area:", circle_obj.area())

create_circle()
