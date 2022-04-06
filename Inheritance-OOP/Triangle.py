from Polygon import Polygon
from Line import Line
from Dot import Dot
import math

class Triangle(Polygon):
    
    def __init__(self, base, height):
        self.__height = height
        self.__base = base
        
    def getArea(self):
        #remember the area of triangle is
        #1/2 * base * height
        base = self.__base.getLength()
        height = self.__height.getLength()
        return (0.5 * base * height)

    def getPerimeter(self):
        #remember that this works on 
        #a RIGHT triangle
        #the formula for triangle's perimeter is
        #a squared + b squared = c squared
        #a = base 
        #b = height 
        base = self.__base.getLength()
        height = self.__height.getLength()
        return  (math.sqrt(
                math.pow(base, 2) 
                + math.pow(height, 2)
                )
                )
        
t = Triangle(Line(Dot(0, 0), Dot(5, 0)), Line(Dot(2, 0), Dot(0, 5)))
print(t.getPerimeter())
print(t.getArea())
