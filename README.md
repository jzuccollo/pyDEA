#pyDEA

Create and solve simple data envelopment analysis problems.

##Installation

###Requires

 - `pyDEA` uses [`PuLP`](http://www.coin-or.org/PuLP/index.html) to solve DEA problems. Install `PuLP` from `PyPI` before proceeding.
 - `pandas`. `pyDEA` uses pandas' dataframes internally to ease integration with data munging in pandas.
 - `statsmodels`. This is used in the `tools` module for regression analyses.
 - `scikit-learn`. Used in the `tools` module for PCA analysis.

###Basic

Download and unpack the files from Github, then run `python setup.py install` in the root directory.

###Pip

To install with `pip` run

    python setup.py sdist
    pip install dist\pydea-X.X.X.zip

where `X.X.X` is the version number.

##Example usage

Using `pyDEA` to solve the initial problem from [this paper](http://www.wbs.ac.uk/downloads/working_papers/352.pdf). See the examples folder for working IPython notebooks.

###Set up the problem

    import pandas as pd
    from pydea import DEA

    inputs = pd.DataFrame([[100, 70], [120, 123], [50, 20], [67, 17], [98, 20], [76, 12]], columns=['Teaching staff', 'Research staff'])
    outputs = pd.DataFrame([[1540, 154, 59], [1408, 186, 23 ], [690, 59, 76], [674, 73, 90], [1686, 197, 12], [982, 63, 15]], columns=['Undergraduates', 'Masters', 'Publications'])

    myprob = DEA(inputs, outputs, kind='VRS')

###Solve the problem and examine the solution

    myprob.solve()

This creates a pandas DataFrame `myprob.results` with the columns `Status`, `Efficiency` and `Weights` that can be easily queried:

    myprob.results[['Status', 'Efficiency']]

returns

    Status  Efficiency
    0  Optimal    1.000000
    1  Optimal    0.815481
    2  Optimal    1.000000
    3  Optimal    1.000000
    4  Optimal    1.000000
    5  Optimal    1.000000

indicating that the problem has been successfully solved for all DMUs. Now examine the efficiency scores:

    myprob.results.Efficiency

returns

    {0: 0.9999999989,
     1: 0.8154810081999999,
     2: 1.0,
     3: 1.000000003,
     4: 1.0000000026,
     5: 1.0}

The calculated weights can be accessed with `myprob.weights` and various elements of the problem are also available as attributes of the `DEA` object.


