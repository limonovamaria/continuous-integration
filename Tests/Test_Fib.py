from src import library as ml
import numpy as np
import pytest


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


