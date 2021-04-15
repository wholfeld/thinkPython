from __future__ import annotations

class Point:
    def __init__(self, x:int, y:int)->Point:
        self.x = x
        self.y = y

    def __str__(self)->str:
        return f'{self.x}, {self.y}'

    def __add__(self:Point, other:Point)->Point:
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other[0], self.y + other[1])

    def __radd__(self:Point, other:tuple)->Point:
        return self.__add__(other)
    
    def print_attributes(self):
        for attr in vars(self):
            print(attr, getattr(self, attr))

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(3, 3)
    p3 = p1 + p2
    p4 = p2 + (2,2)
    p5 = (2,2) + p2
    print(p1)
    print(p3)
    print(p4)
    print(p5)
    print(vars(p1))
    p1.print_attributes()
    print_attributes(p1)
