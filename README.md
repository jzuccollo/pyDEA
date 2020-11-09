# pyDEA

**Not longer actively maintained. [pyDEA](https://github.com/araith/pyDEA) has since been developed. If I were to come back to this, it would make more sense to reimplement it as a pandas-friendly interface for that project.**

Create and solve simple data envelopment analysis problems.

## Installation

This package is written for Python 3.x and does not support Python 2.x.

### Requires

 - `pyDEA` uses [`PuLP`](http://www.coin-or.org/PuLP/index.html) to solve DEA problems. Install `PuLP` from `PyPI` before proceeding.
 - `pandas`. `pyDEA` uses pandas' dataframes internally to ease integration with data munging in pandas.
 - `statsmodels`. This is used in the `tools` module for regression analyses.
 - `scikit-learn`. Used in the `tools` module for PCA analysis.

### Basic

Download and unpack the files from GitHub, then run `python setup.py install` in the root directory.

### Pip

To install with `pip` run

    python setup.py sdist
    pip install dist\pydea-X.X.X.zip

where `X.X.X` is the version number.

## Example usage

See the examples folder for IPython notebooks that illustrate usage.
