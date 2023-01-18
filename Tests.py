from src import MyLibrary as ml
import numpy as np
import pytest


class TestCalculator:

    #подставляем подходящие данные
    def test1(self):
        a = 7
        b = -3
        d = a/b
        assert (ml.Deistvie(a,"/",b) == d)

    # подставляем неподходящие данные
    def test2(self):
        a = 7
        b = -3
        d = 1
        assert (ml.Deistvie(a, "*", b) == d)

    # подставляем данные, которые сломают программу
    def test3(self):
        with pytest.raises(ZeroDivisionError):
            ml.Deistvie(7,"/",0)


class TestFibonachi:

    #подставляем подходящие данные
    def test1(self):
        a = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        assert (ml.Fibonachi(10) == a).all()

    # подставляем неподходящие данные
    def test2(self):
        a = np.array([1])
        assert (len(ml.Fibonachi(1)) == len(a))

    # подставляем данные, которые сломают программу
    def test3(self):
        with pytest.raises(TypeError):
            ml.Fibonachi(-1.2)


class TestPuzirek:

    #подставляем подходящие данные
    def test1(self):
        a = np.array([7,-1,4,13,9])
        b = np.array([13,9,7,4,-1])
        assert (ml.Puzirek(a) == b).all()

    # подставляем неподходящие данные
    def test2(self):
        a = np.array([7, -1, 4, 13, 9])
        b = np.array([9, 7, 13, 4, -1])
        assert (ml.Puzirek(a) == b).all()

    # подставляем данные, которые сломают программу
    def test3(self):
        with pytest.raises(TypeError):
            ml.Puzirek(0)