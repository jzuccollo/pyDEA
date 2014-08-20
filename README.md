#pyDEA

Create and solve simple data envelopment analysis problems.

##Installation

###Requires

`pyDEA` uses [`PuLP`](http://www.coin-or.org/PuLP/index.html) to solve DEA problems. Install `PuLP` from `PyPI` before proceeding.

###Basic

Download and unpack the files from Github, then run `python setup.py install` in the root directory.

###Pip

To install with `pip` run

    python setup.py sdist
    pip install dist\pydea-X.X.X.zip

where `X.X.X` is the version number.

##Example usage

Using `pyDEA` to solve the initial problem from [this paper](http://www.wbs.ac.uk/downloads/working_papers/352.pdf).

###Set up the problem

    import numpy as np
    from pydea import DEA

    inputs = np.array([[100, 70], [120, 123], [50, 20], [67, 17], [98, 20], [76, 12]])
    outputs = np.array([[1540, 154, 59], [1408, 186, 23 ], [690, 59, 76], [674, 73, 90], [1686, 197, 12], [982, 63, 15]])

    myprob = DEA(inputs, outputs, kind='VRS')

###Solve the problem and examine the solution

    myprob.solve()

    myprob.status

returns

    {0: 'Optimal',
     1: 'Optimal',
     2: 'Optimal',
     3: 'Optimal',
     4: 'Optimal',
     5: 'Optimal'}

indicating that the problem has been successfully solved for all DMUs. Now examine the efficiency scores:

    myprob.efficiency

returns

    {0: 0.9999999989,
     1: 0.8154810081999999,
     2: 1.0,
     3: 1.000000003,
     4: 1.0000000026,
     5: 1.0}

The calculated weights can be accessed with `myprob.weights` and various elements of the problem are also available as attributes of the `DEA` object.


