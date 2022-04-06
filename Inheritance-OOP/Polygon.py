from abc import ABCMeta, abstractmethod
from Line import Line

#this class that are used to ensure that
#every class that inherit this class would have
#all the method that are available here
class Polygon(Line, metaclass = ABCMeta):
    
    #abstract method, used to ensure that 
    #the inherited class will have this 
    #getArea method
    @abstractmethod
    def getArea(self):
        pass
    def getPerimeter(self):
        pass
