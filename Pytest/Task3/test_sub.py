from cmplex import C
from random import randint

# Napisać testy sprawdzające odejmowanie liczb zespolonych
# w załączonym pliku
class MiniTesty:
    def test1(self):
        assert C(0, 0) - C(0, 0) == C(0, 0)

    def test2(self):
        assert C(1, 1) - C(-1, -1) == C(2, 2)

    def test3(self):
        assert C(1, -1) - C(1, -1) == C(0, 0)

    def test4(self):
        x1 = randint(-100, 100)
        y1 = randint(-100, 100)
        x2 = randint(-100, 100)
        y2 = randint(-100, 100)

        assert C(x1, y1) - C(x2, y2) == C(x1 - x2, y1 - y1)

class MaxiTesty:
    def testM1(self):
        x1 = randint(-10**12, 10**12)
        y1 = randint(-10**12, 10**12)
        x2 = randint(-10**12, 10**12)
        y2 = randint(-10**12, 10**12)  
        assert C(x1, y1) - C(x2, y2) == C(x1 - x2, y1 - y1)
    
    def testM2(self):
        x1 = randint(-10**13, 10**13)
        y1 = randint(-10**13, 10**13)
        x2 = randint(-10**13, 10**13)
        y2 = randint(-10**13, 10**13) 
        assert C(x1, y1) - C(x2, y2) == C(x1 - x2, y1 - y1)
    def testM3(self):
        x1 = randint(-10**14, 10**14)
        y1 = randint(-10**14, 10**14)
        x2 = randint(-10**14, 10**14)
        y2 = randint(-10**14, 10**14) 
        assert C(x1, y1) - C(x2, y2) == C(x1 - x2, y1 - y1)

    def testM4(self):
        x1 = randint(-10**13, -10**13)
        y1 = randint( 10**13, 10**13)
        x2 = randint( 10**14, -10**13)
        y2 = randint(-10**13, -10**14)  
        assert C(x1, y1) - C(x2, y2) == C(x1 - x2, y1 - y1)