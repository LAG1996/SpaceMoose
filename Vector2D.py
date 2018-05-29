import math
from BaseClass import BaseClass

class Vector2D(BaseClass):
    def __init__(self, xy, id = ""):
        self.x = xy[0]
        self.y = xy[1]
        super(Vector2D, self).__init__(id)


    #adds two vectors and then returns the resulting vector
    def add(self, other):
        return Vector2D((self.x + other.x, self.y + other.y))

    #finds difference between two vectors and then returns the resulting vector
    def subtract(self, other):
        return Vector2D((self.x - other.x, self.y - other.y))

    #scales elements of vectors and returns the resulting vector
    def scale(self, scalar):
        return Vector2D((self.x * scalar, self.y * scalar))

    #normalizes the vector and returns the resulting vector
    def normalize(self):
        if self.magnitude() == 0:
            return Vector2D((0,0))
        else:
            return Vector2D((self.x/self.magnitude(), self.y/self.magnitude()))

    #uses math.sqrt from the math class, which was imported in header
    #returns the vectors magnitude
    def magnitude(self):
        return float(math.sqrt((self.x*self.x) + (self.y*self.y)))

    #overload return-this-as-string for printing
    def __str__(self):
        return ("{},{}").format(self.x, self.y)

    


