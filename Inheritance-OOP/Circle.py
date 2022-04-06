from Dot import Dot
from Line import Line
from Polygon import Polygon

class Circle(Polygon):
    def __init__(self, radius):
        self.__radius = radius
        
    def getArea(self):
        #remember the formula for finding 
        #the area of a circle is
        #pi * r * r
        pi = 3.14
        radius = self.__radius.getLength()
        return (pi * radius * radius)
    
    def getPerimeter(self):
        #remember the formula for finding
        #the perimeter of a circle is
        #2 * pi * r
        pi = 3.14
        radius = self.__radius.getLength()
        return (2 * pi * radius)

c = Circle(Line(Dot(0, 0), Dot(0, 5)))
print(c.getArea())
print(c.getPerimeter())
