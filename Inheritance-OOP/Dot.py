class Dot:
    #class attribute
    class_name = "Dot class"
    
    #static method
    @staticmethod
    def info():
        return Dot.class_name
    
    #constructor method (initialization)
    def __init__(self, x = 0, y = 0):
        #private variables start with __(double underscores)
        #protected variables start with _ (single underscore)
        self.__x = x
        self.__y = y
    
    #creating setter
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y
        
    #creating getter
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y

    #user defined methods
    def showCoordinates(self):
        return '{} {}'.format(self.__x, self.__y)
    
    def showDotPosition(self):
        return 'Dot with coordinates {}'.format(self.showCoordinates())
    
    #to string method
    def __str__(self):
        return self.showDotPosition()
    
    
d = Dot()
d.setX(12)
d.setY(15)
print(d.showCoordinates())
print(d.showDotPosition())
