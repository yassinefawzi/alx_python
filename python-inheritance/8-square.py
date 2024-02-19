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
    
    """"defining our function area"""
    def area(self):
        return self.__width * self.__height
    
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

"""defining our class Rectangle"""
class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    """"defining our function area"""
    def area(self):
        return self.__size ** 2