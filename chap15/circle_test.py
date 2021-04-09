from Circle import Point, Circle, Rectangle, distance, point_in_circle, rect_and_circle_overlap, rect_in_circle
import unittest

class Test_Circle(unittest.TestCase):

    def test_distance(self):
        p1 = Point(3, 3)
        p2 = Point(0, 3)
        p3 = Point(3, 3)
        self.assertEqual(distance(p1, p2), 3)
        self.assertNotEqual(distance(p1, p3), 3)
    
    def test_point_in_circle(self):
        circle = Circle(Point(3, 3), 3)
        p1 = Point(3, 2)
        p2 = Point(8, -1)
        self.assertTrue(point_in_circle(circle, p1))
        self.assertFalse(point_in_circle(circle, p2))
    
    def test_rect_get_points(self):
        rect = Rectangle(Point(1, 1), 2, 2)
        points = rect.get_points()
        self.assertEqual(points[0].x, 1,)
        self.assertEqual(points[0].y, 1,)
        self.assertEqual(points[3].x, 3,)
        self.assertEqual(points[3].y, -1,)
        self.assertNotEqual(points[1].y, -1,)
        # for point in points:
        #     print(f'{point.x} {point.y}')
    

    def test_rect_in_circle(self):
        circle = Circle(Point(5, 5), 5)
        rect = Rectangle(Point(3, 5), 4, 4)
        rect2 = Rectangle(Point(-30, 5), 4, 4)
        self.assertTrue(rect_in_circle(circle, rect))
        self.assertFalse(rect_in_circle(circle, rect2))
    
    def test_rect_and_circle_overlap(self):
        circle = Circle(Point(7, 3), 2.5)
        circle2 = Circle(Point(7, 3), 1.5)
        rect = Rectangle(Point(0, 5), 5, 5)
        self.assertTrue(rect_and_circle_overlap(circle, rect))
        self.assertFalse(rect_and_circle_overlap(circle2, rect))

if __name__ == '__main__':
    unittest.main()