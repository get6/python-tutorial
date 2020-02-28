import unittest
import myCalc

class MyCalcTest(unittest.TestCase):

    def test_add(self):
        c = myCalc.add(20, 10)
        self.assertEqual(c, 30)

    def test_substract(self):
        c = myCalc.substract(20, 10)
        self.assertEqual(c, 10)

    # test_로 시작되지 않는 함수는 실행되지 않음
    def hi(self):
        print(123)

if __name__ == '__main__':
    unittest.main()