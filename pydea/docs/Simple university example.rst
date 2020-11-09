Simple university example
=========================

Drawn from `this
paper <http://www.wbs.ac.uk/downloads/working_papers/352.pdf>`__ and
augmented to allow correlation with environmental variables.

Create the input data
---------------------

Data is constructed as a ``pandas`` dataframe.

.. code:: ipython3

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pydea
    
    %matplotlib inline
    
    inputs = pd.DataFrame([[100, 70], [120, 123], [50, 20], [67, 17], [98, 20], [76, 12]], columns=['Teaching staff', 'Research staff'])
    outputs = pd.DataFrame([[1540, 154, 59], [1408, 186, 23 ], [690, 59, 76], [674, 73, 90], [1686, 197, 12], [982, 63, 15]], columns=['Undergraduates', 'Masters', 'Publications'])
    env_vars = pd.DataFrame([[  5.15262633e+00,   5.25431862e+03],
           [  8.62019738e+00,   1.10390901e+04],
           [  3.95821220e+00,   5.88356035e+03],
           [  9.21476691e+00,   1.54834181e+03],
           [  2.96674662e-01,   1.40433297e+04],
           [  1.41538397e+01,   3.75047428e+03]], columns=['Funding', 'City_size'])

.. code:: ipython3

    inputs




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Teaching staff</th>
          <th>Research staff</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>100</td>
          <td>70</td>
        </tr>
        <tr>
          <th>1</th>
          <td>120</td>
          <td>123</td>
        </tr>
        <tr>
          <th>2</th>
          <td>50</td>
          <td>20</td>
        </tr>
        <tr>
          <th>3</th>
          <td>67</td>
          <td>17</td>
        </tr>
        <tr>
          <th>4</th>
          <td>98</td>
          <td>20</td>
        </tr>
        <tr>
          <th>5</th>
          <td>76</td>
          <td>12</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    outputs




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Undergraduates</th>
          <th>Masters</th>
          <th>Publications</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>1540</td>
          <td>154</td>
          <td>59</td>
        </tr>
        <tr>
          <th>1</th>
          <td>1408</td>
          <td>186</td>
          <td>23</td>
        </tr>
        <tr>
          <th>2</th>
          <td>690</td>
          <td>59</td>
          <td>76</td>
        </tr>
        <tr>
          <th>3</th>
          <td>674</td>
          <td>73</td>
          <td>90</td>
        </tr>
        <tr>
          <th>4</th>
          <td>1686</td>
          <td>197</td>
          <td>12</td>
        </tr>
        <tr>
          <th>5</th>
          <td>982</td>
          <td>63</td>
          <td>15</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    env_vars




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Funding</th>
          <th>City_size</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>5.152626</td>
          <td>5254.31862</td>
        </tr>
        <tr>
          <th>1</th>
          <td>8.620197</td>
          <td>11039.09010</td>
        </tr>
        <tr>
          <th>2</th>
          <td>3.958212</td>
          <td>5883.56035</td>
        </tr>
        <tr>
          <th>3</th>
          <td>9.214767</td>
          <td>1548.34181</td>
        </tr>
        <tr>
          <th>4</th>
          <td>0.296675</td>
          <td>14043.32970</td>
        </tr>
        <tr>
          <th>5</th>
          <td>14.153840</td>
          <td>3750.47428</td>
        </tr>
      </tbody>
    </table>
    </div>



Build and solve the DEA object
------------------------------

.. code:: ipython3

    uni_prob = pydea.DEAProblem(inputs, outputs, returns='CRS')

.. code:: ipython3

    myresults = uni_prob.solve()

Results
-------

.. code:: ipython3

    myresults['Status']




.. parsed-literal::

    0    Optimal
    1    Optimal
    2    Optimal
    3    Optimal
    4    Optimal
    5    Optimal
    Name: Status, dtype: object



.. code:: ipython3

    myresults['Efficiency']




.. parsed-literal::

    0    0.961991
    1    0.798801
    2    1.000000
    3    1.000000
    4    1.000000
    5    1.000000
    Name: Efficiency, dtype: float64



.. code:: ipython3

    myresults['Weights']




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>in_Teaching staff</th>
          <th>in_Research staff</th>
          <th>out_Undergraduates</th>
          <th>out_Masters</th>
          <th>out_Publications</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>0.010000</td>
          <td>0.000000</td>
          <td>0.000571</td>
          <td>0.000000</td>
          <td>0.001392</td>
        </tr>
        <tr>
          <th>1</th>
          <td>0.008333</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.004001</td>
          <td>0.002377</td>
        </tr>
        <tr>
          <th>2</th>
          <td>0.020000</td>
          <td>0.000000</td>
          <td>0.001143</td>
          <td>0.000000</td>
          <td>0.002783</td>
        </tr>
        <tr>
          <th>3</th>
          <td>0.000000</td>
          <td>0.058824</td>
          <td>0.000000</td>
          <td>0.005570</td>
          <td>0.006593</td>
        </tr>
        <tr>
          <th>4</th>
          <td>0.000000</td>
          <td>0.050000</td>
          <td>0.000499</td>
          <td>0.000484</td>
          <td>0.005317</td>
        </tr>
        <tr>
          <th>5</th>
          <td>0.000000</td>
          <td>0.083333</td>
          <td>0.000878</td>
          <td>0.000000</td>
          <td>0.009163</td>
        </tr>
      </tbody>
    </table>
    </div>



Distribution of efficiency scores
---------------------------------

.. code:: ipython3

    myresults['Efficiency'].hist(bins=50)
    plt.ylabel('Frequency')
    plt.xlabel('Efficiency score')
    plt.title('Distribution of efficiency scores')




.. parsed-literal::

    Text(0.5, 1.0, 'Distribution of efficiency scores')




.. image:: Simple%20university%20example_files/Simple%20university%20example_13_1.png


Correlation with environment variables
--------------------------------------

.. code:: ipython3

    myresults.env_corr(env_vars)


.. parsed-literal::

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:             Efficiency   R-squared:                       0.410
    Model:                            OLS   Adj. R-squared:                  0.017
    Method:                 Least Squares   F-statistic:                     1.042
    Date:                Mon, 09 Nov 2020   Prob (F-statistic):              0.453
    Time:                        14:37:53   Log-Likelihood:                 8.7340
    No. Observations:                   6   AIC:                            -11.47
    Df Residuals:                       3   BIC:                            -12.09
    Df Model:                           2                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept      1.1259      0.122      9.217      0.003       0.737       1.515
    Funding       -0.0105      0.009     -1.119      0.345      -0.040       0.019
    City_size  -1.351e-05   9.61e-06     -1.407      0.254   -4.41e-05    1.71e-05
    ==============================================================================
    Omnibus:                          nan   Durbin-Watson:                   0.782
    Prob(Omnibus):                    nan   Jarque-Bera (JB):                0.359
    Skew:                          -0.040   Prob(JB):                        0.836
    Kurtosis:                       1.804   Cond. No.                     3.06e+04
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 3.06e+04. This might indicate that there are
    strong multicollinearity or other numerical problems.


.. parsed-literal::

    /Users/jameszuccollo/miniconda3/envs/analysis/lib/python3.7/site-packages/statsmodels/stats/stattools.py:75: ValueWarning: omni_normtest is not valid with less than 8 observations; 6 samples were given.
      "samples were given." % int(n), ValueWarning)




.. parsed-literal::

    <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x7fc0074c5650>



