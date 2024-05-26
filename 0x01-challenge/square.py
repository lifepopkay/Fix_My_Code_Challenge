#!/usr/bin/python3
"""
    Calculations on a square

    Returns:Area  or perimeter
"""
    
    
class Square():
    """ 
        class of a square
    """

    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            self.width = kwargs.get('width', 0)
            self.height = kwargs.get('height', 0)
            if self.width != self.height:
                raise ValueError("The width and height must be equal")
    
    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
