
import nose
import numpy as np
import pandas as pd
from pydea.dea import *
from numpy.testing import assert_array_equal


class TestDEAProblem():
    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""
        cls.inputs = pd.DataFrame([[100, 70], [120, 123], [50, 20], [67, 17], [98, 20], [76, 12]])
        cls.outputs = pd.DataFrame([[1540, 154, 59], [1408, 186, 23 ], [690, 59, 76], [674, 73, 90], [1686, 197, 12], [982, 63, 15]])

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        pass

    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        pass

    def test_init_attributes(self):
        """Test attributes of init"""
        myprob = DEAProblem(self.inputs, self.outputs)
        np.testing.assert_array_equal(myprob.inputs, self.inputs)
        np.testing.assert_array_equal(myprob.outputs, self.outputs)
        nose.tools.assert_equal(myprob.J, 6)
        nose.tools.assert_equal(myprob.I, 2)
        nose.tools.assert_equal(myprob.R, 3)

    @nose.tools.raises(AssertionError)
    def test_init_asserts(self):
        """Test asserts of init"""
        myprob = DEAProblem(pd.DataFrame([[100]]), pd.DataFrame([[1], [2]]))


class TestDEAResults():
    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""
        cls.inputs = pd.DataFrame([[100, 70], [120, 123], [50, 20], [67, 17], [98, 20], [76, 12]])
        cls.outputs = pd.DataFrame([[1540, 154, 59], [1408, 186, 23 ], [690, 59, 76], [674, 73, 90], [1686, 197, 12], [982, 63, 15]])
        myprob = DEAProblem(self.inputs, self.outputs)
        myres = myprob.solve()

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        pass

    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        pass

    def test_init_attributes(self):
        """Test attributes of init"""
        pass
