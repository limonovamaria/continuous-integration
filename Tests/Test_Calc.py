from src import MyLibrary as ml
import numpy as np
import pytest


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
