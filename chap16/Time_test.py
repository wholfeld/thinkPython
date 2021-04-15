import unittest
from Time import Time, mul_time, average_pace

class Test_Time(unittest.TestCase):

    def test_multiply(self):
        t1 = Time()
        t1.hour = 2
        t1.minute = 30
        t1.second = 0
        t2 = mul_time(t1, 2)
        self.assertEqual(t2.minute, 0)
        self.assertEqual(t2.hour, 5)

    def test_average_pace(self):
        t1 = Time()
        t1.hour = 2
        t1.minute = 30
        t1.second = 0
        t2 = average_pace(t1, 5)
        self.assertEqual(t2.hour, 0)
        self.assertEqual(t2.minute, 30)

if __name__ == '__main__':
    unittest.main()