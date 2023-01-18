from src import MyLibrary as ml
import numpy as np
import pytest


class PuzTest:


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