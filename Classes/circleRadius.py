import math
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi*self.radius**2
    
aCircle = Circle(5)
print(f"{aCircle.area():.2f}")

''' Class for Rectangle '''

class Rectangle(object):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    
    def area(self):
        return self.l * self.b
    
aRectangle = Rectangle(2, 10)
print(aRectangle.area())

'''
Define a class named Shape and its subclass Square. 

The Square class has an init function which takes a length as argument. 

Both classes have a area function which can print the area of the shape 
where Shape's area is 0 by default.
'''

class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
    

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length ** 2
    
aSquare = Square(3)
print(aSquare.area())