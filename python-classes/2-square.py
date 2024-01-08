"defining a class named square"
class Square:

    "assigning prive attribute to the class"
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    "area method that return the square root"
    def area(self):
        return self.__size ** 2