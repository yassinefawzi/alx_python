"""defining our class BaseGeometry"""

class BaseGeometry:
    """"defining our function area"""
    def area(self):
        raise Exception("area() is not implemented")
    
    """"defining our function intiger_validator that check the values of our int"""
    def integer_validator(self, name, value):
        if isinstance(value, int) != True:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")

"""defining our class Rectangle"""
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)