import math

class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    
class Circle:
    def __init__(self, center:Point, radius:float):
        self.center = center
        self.radius = radius
        self.get_points_360()
    
    def get_points_360(self):
        points = []
        rad_90 = []
        radius = self.radius
        center_x = self.center.x
        center_y = self.center.y
        for i in range(91):
            rad_90.append(0 + i/90*radius)
        for y in rad_90:
            x = solve_pathag(y, radius)
            points.append(Point(center_x + x, center_y + y))
            points.append(Point(center_x - x, center_y + y))
            points.append(Point(center_x + x, center_y - y))
            points.append(Point(center_x - x, center_y - y))
        # for point in points:
        #     print(f'{point.x} {point.y}')
        return points

class Rectangle:
    def __init__(self, topLeftPoint:Point, width:float, height:float):
        self.topLeftPoint = topLeftPoint
        self.width = width
        self.height = height
    
    def get_points(self)->tuple:
        topLeftX = self.topLeftPoint.x
        topLeftY = self.topLeftPoint.y
        botLeftPoint = Point(topLeftX, topLeftY - self.height)
        topRightPoint = Point(topLeftX + self.width, topLeftY)
        botRightPoint = Point(topLeftX + self.width, topLeftY - self.height)
        return (self.topLeftPoint, topRightPoint, botLeftPoint, botRightPoint)

def distance(p1:Point, p2:Point)->float:
    x_dif = abs(p1.x - p2.x)
    y_dif = abs(p1.y - p2.y)
    result = math.sqrt(x_dif**2 + y_dif**2)
    return result

def point_in_circle(circle:Circle, point:Point)->bool:
    # print(circle.radius)
    # print(int(distance(point, circle.center)))
    return circle.radius > int(distance(point, circle.center))

def rect_in_circle(circle:Circle, rectangle:Rectangle)->bool:
    points = rectangle.get_points()
    for point in points:
        if point_in_circle(circle, point):
            return True

    return False

def rect_and_circle_overlap(circle:Circle, rectangle:Rectangle)->bool:
    circle_points = circle.get_points_360()
    rect_points = rectangle.get_points()
    top_left = rect_points[0]
    bot_right = rect_points[3]
    for point in circle_points:
        if point.x >= top_left.x and point.x <= bot_right.x:
            if point.y >= bot_right.y and point.y <= top_left.y:
                # print(f'{point.x} {point.y}')
                return True
    return False


def solve_pathag(b:float, c:float):
    a = c**2 - b**2
    a = math.sqrt(a)
    return a

if __name__ == '__main__':
    circle = Circle(Point(5, 5), 5)
    points = circle.get_points_360()
    # print(solve_pathag(3, 5))
    # print(solve_pathag(4, 5))