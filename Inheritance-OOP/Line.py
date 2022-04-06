from Dot import Dot
import math

#line class
class Line(Dot):
    def __init__(self, t1, t2):
        self.__t1 = t1
        self.__t2 = t2
    
    #setter method
    def setInitialDot(self, t1):
        self.__t1 = t1
    
    def setTerminatingDot(self, t2):
        self.__t2 = t2
    
    #getter method
    def getInitialDot(self):
        return self.__t1
    
    def getTerminatingDot(self):
        return self.__t2
    
    #user defined methods
    def getLength(self):
        #remember, the formula for finding the length in diagonal lines is:
        #square root of (x2 - x1) squared + (y2 - y1) squared
        x1 = self.__t1.getX()
        x2 = self.__t2.getX()
        y1 = self.__t1.getY()
        y2 = self.__t2.getY()
        
        #pythonicness
        return  (math.sqrt
                (math.pow((x2 - x1), 2)) 
                + (math.pow((y2 - y1), 2))
                )
        
    def __str__(self):
        return self.getLength()

l = Line(Dot(0, 0), Dot(0, 5))
print(l.getLength())
