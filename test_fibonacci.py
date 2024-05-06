import unittest #built-in function
import fibonacciseries

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_with_positive_input(self):
        number = 10
        result = fibonacciseries.fibonacci_series(number)
        assert result==[0,1,1,2,3,5,8,13,21,34]

        number = 5
        result = fibonacciseries.fibonacci_series(number)
        assert result==[0,1,1,2,3]


    def test_fibonacci_with_negative_input(self):
        pass
        number = -5
        result = fibonacciseries.fibonacci_series(number)
        assert result is None


    def test_fibonacci_with_zero_input(self):
        number = 0
        result = fibonacciseries.fibonacci_series(number)
        assert result is None


    def test_fibonacci_with_one_input(self):
        number = 1
        result = fibonacciseries.fibonacci_series(number)
        assert result==[0]

    def test_fibonacci_with_two_input(self):
        number = 2
        result = fibonacciseries.fibonacci_series(number)
        assert result==[0,1]

    def test_fibonacci_with_wrong_input_type(self):
        number = .1
        result = fibonacciseries.fibonacci_series(number)
        assert result is None


unittest.main()