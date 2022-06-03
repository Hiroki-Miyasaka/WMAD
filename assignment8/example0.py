# problem 0
# Create a Cricle class and initialize it with radius. Make two instance methods getArea 
# and getCircumference inside this class. Implement the methods.
# No need to write test class or main function for this.

class Circle:
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        return self.radius*self.radius*Circle.PI
    
    def getCircumFerence(self):
        return 2*Circle.PI*self.radius

circle = Circle(5)
print(circle.getArea())
print(circle.getCircumFerence())