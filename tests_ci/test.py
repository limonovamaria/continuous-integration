from src import library as ml
import pytest
import numpy as np


class Test_Calc:

    def test1(self):
        a = 7
        b = -3
        d = a/b
        assert (ml.Deistvie(a,"/",b) == d)

    def test2(self):
        a = 7
        b = -3
        d = a+b
        assert (ml.Deistvie(a, "+", b) == d)

    def test3(self):
        with pytest.raises(ZeroDivisionError):
            ml.Deistvie(7,"/",0)


class Test_Fib:

    def test1(self):
        a = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        assert (ml.Fibonachi(10) == a).all()

    def test2(self):
        a = np.array([1,1])
        assert (len(ml.Fibonachi(2)) == len(a))

    def test3(self):
        with pytest.raises(TypeError):
            ml.Fibonachi(-1.2)


class Test_Puz:

    def test1(self):
        a = np.array([7,-1,4,13,9])
        b = np.array([13,9,7,4,-1])
        assert (ml.Puzirek(a) == b).all()

    def test2(self):
        a = np.array([1, 9, -1, 5, 8])
        b = np.array([9, 8, 5, 1, -1])
        assert (ml.Puzirek(a) == b).all()

    def test3(self):
        with pytest.raises(TypeError):
            ml.Puzirek(0)