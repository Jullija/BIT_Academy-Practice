from function import is_prime
from correct_function import is_prime2
from random import randint

class TestMini:
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>
    def from_minus_to_six():

        for i in range (-1, 7):
            if i == -1 or i == 0 or i == 1 or i == 4 or i == 6:
                assert is_prime(i) == False 
            else:
                assert is_prime(i) == True

        # def test1():
        #     assert is_prime(-1) == False
        # def test2():
        #     assert is_prime(0) == False
        # def test3():
        #     assert is_prime(1) == False
        # def test4():
        #     assert is_prime(2) == True
        # def test5():
        #     assert is_prime(3) == True
        # def test6():
        #     assert is_prime(4) == False
        # def test7():
        #     assert is_prime(5) == True
        # def test8():
        #     assert is_prime(6) == False

class TestMid:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>
    def test_mid1(self):
        assert is_prime(10**4) == is_prime2(10**4)
    def test_mid2(self):
        assert is_prime(10**5) == is_prime2(10**5)
    def test_mid3(self):
        num = randint(10**4, 10**5)
        assert is_prime(num) == is_prime2(num)
    def test_mid4(self):
        num = randint(10**4, 10**5)
        assert is_prime(num) == is_prime2(num)
    def test_mid5(self):
        num = randint(10**4, 10**5)
        assert is_prime(num) == is_prime2(num)



class TestMaxi:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji
    def test_maxi1(self):
        assert is_prime(10**12) == is_prime2(10**12)
    def test_maxi2(self):
        assert is_prime(10**13) == is_prime2(10**13)
    def test_maxi3(self):
        num = randint(10**12, 10**13)
        assert is_prime(num) == is_prime2(num)
    def test_maxi4(self):
        num = randint(10**12, 10**13)
        assert is_prime(num) == is_prime2(num)
    def test_maxi5(self):
        num = randint(10**12, 10**13)
        assert is_prime(num) == is_prime2(num)
