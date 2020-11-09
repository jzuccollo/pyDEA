import numpy as np
import pandas as pd
import pytest
from pydea.dea import *
from numpy.testing import assert_array_equal


@pytest.fixture(scope='function')
def dummy_data():
    """This function is run once before any tests are run"""
    inputs = pd.DataFrame([[100, 70], [120, 123], [50, 20],
        [67, 17], [98, 20], [76, 12]])
    outputs = pd.DataFrame([[1540, 154, 59], [1408, 186, 23],
        [690, 59, 76], [674, 73, 90], [1686, 197, 12], [982, 63, 15]])
    return inputs, outputs

def test_init_attributes(dummy_data):
    """Test attributes of init"""
    inputs, outputs = dummy_data
    myprob = DEAProblem(inputs, outputs)
    np.testing.assert_array_equal(myprob.inputs, inputs)
    np.testing.assert_array_equal(myprob.outputs, outputs)
    assert myprob.J == 6
    assert myprob.I == 2
    assert myprob.R == 3

def test_init_asserts():
    """Test asserts"""
    with pytest.raises(AssertionError):
        DEAProblem(pd.DataFrame([[100]]), pd.DataFrame([[1], [2]]))
