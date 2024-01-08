"defining a class named square"
class Square:

    "assigning prive attribute to the class"
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
        "getter and setter methods"
        @property
        def size(self):
            return self.__size
        @size.setter
        def size(self, value):
            if not isinstance(value,int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    "area method that return the square root"     
    def area(self):
        return self.__size ** 2
    "my print method which print the square with # charachter"
    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()