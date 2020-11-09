DEA of English schools
======================

Use the DEA module to examine the relative performance of English
schools.

.. code:: ipython3

    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pydea as dea
    import pandas as pd
    
    %matplotlib inline

##Import the data

Retrieve results and financial data from the DfE website and read in to
a pandas DataFrame object. For now, ignore the list of open academies.

-  `School performance tables and financial
   data <http://www.education.gov.uk/schools/performance/download_data.html>`__
-  `Open
   academies <https://www.gov.uk/government/publications/open-academies-and-academy-projects-in-development>`__

Read data
~~~~~~~~~

.. code:: ipython3

    import os
    import pickle
    import requests
    from zipfile import ZipFile
    from io import BytesIO
    
    def cached_data(picklename, genfunc):
        cache_path = picklename + ".pickle"
        if not os.path.exists(cache_path):
            # The cache doesn't exist, create it and populate it
            result = genfunc() 
            cache_file = open(cache_path,'wb')
            # Write it to the result to the file as a pickled object
            # Use the binary protocol for better performance
            pickle.dump(result, cache_file, protocol=1)
            cache_file.close()
        return pickle.load(open(cache_path,'rb'))
    
    
    #    These functions actually generates the data when it isn't cached.
    #    The data generated is often expensive to compute so caching helps with performance.
    
    def gen_results():
           
        #Results data    
        dfe_results_urls = ['http://www.education.gov.uk/schools/performance/download/csv/england_ks2.csv',
                        'http://www.education.gov.uk/schools/performance/download/csv/england_ks4.csv',
                        'http://www.education.gov.uk/schools/performance/download/csv/england_ks5.csv',
                        'http://www.education.gov.uk/schools/performance/download/csv/england_abs.csv',
                        'http://www.education.gov.uk/schools/performance/download/csv/england_cfr.csv',
                        'http://www.education.gov.uk/schools/performance/download/csv/england_swf.csv',
                        'http://www.education.gov.uk/schools/performance/download/csv/england_spine.csv',
                        'http://www.education.gov.uk/schools/performance/download/csv/england_census.csv']
    
        dfe_results_dfs = []
        for url in dfe_results_urls[0:1]:
            tmpdf = pd.read_csv(url, na_values=['PRI', 'SEC', 'NAT', 'NA', 'NP', 'SUPP', 'NE', 'NEW', 'LOWCOV'], index_col=4)
            dfe_results_dfs.append(tmpdf)
            
        return dfe_results_dfs
    
    def gen_findat():
        
        #Financial data
        zipFileURL = "http://www.education.gov.uk/schools/performance/download/School_total_spend_2012-2013-Full_data_workbook.zip"
    
        DfEzip = requests.get(zipFileURL)
        DfEfindat = ZipFile(BytesIO(DfEzip.content), 'r')
        findat = pd.read_excel(DfEfindat.open(DfEfindat.namelist()[0]), 2,
                              skiprows=3,
                              index_col=6,
                              na_values=['PRI', 'SEC', 'NAT', 'NA', 'NP', 'SUPP', 'NE', 'NEW', 'LOWCOV'])
    
        return findat
    
    dfe_results_dfs = cached_data("dfe_results", gen_results)
    findat = cached_data("dfe_findat", gen_findat)

Results data
~~~~~~~~~~~~

.. code:: ipython3

    ks2res = dfe_results_dfs[0]
    ks2res.describe().T[:5]




.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>count</th>
          <th>mean</th>
          <th>std</th>
          <th>min</th>
          <th>25%</th>
          <th>50%</th>
          <th>75%</th>
          <th>max</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>RECTYPE</th>
          <td> 16190</td>
          <td>     1.061519</td>
          <td>     0.278619</td>
          <td>    1</td>
          <td>     1.0</td>
          <td>     1.0</td>
          <td>     1.0</td>
          <td>      5</td>
        </tr>
        <tr>
          <th>ALPHAIND</th>
          <td> 16036</td>
          <td> 30921.753430</td>
          <td> 17294.515442</td>
          <td>   20</td>
          <td> 15975.5</td>
          <td> 31525.0</td>
          <td> 45922.5</td>
          <td>  60290</td>
        </tr>
        <tr>
          <th>LEA</th>
          <td> 16188</td>
          <td>   696.975908</td>
          <td>   262.743650</td>
          <td>  201</td>
          <td>   371.0</td>
          <td>   850.0</td>
          <td>   891.0</td>
          <td>    938</td>
        </tr>
        <tr>
          <th>ESTAB</th>
          <td> 16036</td>
          <td>  2962.048017</td>
          <td>  1135.598625</td>
          <td> 2000</td>
          <td>  2127.0</td>
          <td>  2694.5</td>
          <td>  3344.0</td>
          <td>   7749</td>
        </tr>
        <tr>
          <th>URN_AC</th>
          <td> 16036</td>
          <td>  3313.438202</td>
          <td> 21240.185772</td>
          <td>    0</td>
          <td>     0.0</td>
          <td>     0.0</td>
          <td>     0.0</td>
          <td> 140120</td>
        </tr>
      </tbody>
    </table>
    </div>



Financial data
~~~~~~~~~~~~~~

This is a fragile procedure with a lot of hard-coded parts. **Check the
data before proceeding**.

.. code:: ipython3

    findat.describe().T[:5]




.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>count</th>
          <th>mean</th>
          <th>std</th>
          <th>min</th>
          <th>25%</th>
          <th>50%</th>
          <th>75%</th>
          <th>max</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>LA code</th>
          <td> 18114</td>
          <td>     701.145854</td>
          <td>     260.996499</td>
          <td>     201</td>
          <td>     372.00</td>
          <td>     850.0</td>
          <td>     891</td>
          <td>     938</td>
        </tr>
        <tr>
          <th>Estab code</th>
          <td> 18114</td>
          <td>    3091.494645</td>
          <td>    1197.294631</td>
          <td>    2000</td>
          <td>    2165.00</td>
          <td>    2982.5</td>
          <td>    3424</td>
          <td>    7750</td>
        </tr>
        <tr>
          <th>School DfE number</th>
          <td> 18114</td>
          <td> 7014550.035001</td>
          <td> 2609976.801063</td>
          <td> 2013614</td>
          <td> 3722104.25</td>
          <td> 8502749.5</td>
          <td> 8912894</td>
          <td> 9387022</td>
        </tr>
        <tr>
          <th>School statutory low age</th>
          <td> 18114</td>
          <td>       4.692006</td>
          <td>       2.362017</td>
          <td>       2</td>
          <td>       3.00</td>
          <td>       4.0</td>
          <td>       5</td>
          <td>      14</td>
        </tr>
        <tr>
          <th>School statutory high age</th>
          <td> 18114</td>
          <td>      11.402782</td>
          <td>       2.485372</td>
          <td>       5</td>
          <td>      11.00</td>
          <td>      11.0</td>
          <td>      11</td>
          <td>      19</td>
        </tr>
      </tbody>
    </table>
    </div>



Merge datasets on school’s URN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For now, deal with only primary schools and their KS2 results

.. code:: ipython3

    prim_findat = findat[findat['Phase of education'] == 'Primary']
    primdat = prim_findat.join(ks2res)
    primdat.describe().T[:5]




.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>count</th>
          <th>mean</th>
          <th>std</th>
          <th>min</th>
          <th>25%</th>
          <th>50%</th>
          <th>75%</th>
          <th>max</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>LA code</th>
          <td> 15615</td>
          <td>     705.823567</td>
          <td>     259.200834</td>
          <td>     201</td>
          <td>     373.0</td>
          <td>     850</td>
          <td>     891.0</td>
          <td>     938</td>
        </tr>
        <tr>
          <th>Estab code</th>
          <td> 15615</td>
          <td>    2739.930772</td>
          <td>     693.918032</td>
          <td>    2000</td>
          <td>    2130.0</td>
          <td>    2508</td>
          <td>    3306.0</td>
          <td>    5949</td>
        </tr>
        <tr>
          <th>School DfE number</th>
          <td> 15615</td>
          <td> 7060975.601601</td>
          <td> 2592077.227001</td>
          <td> 2013614</td>
          <td> 3732324.5</td>
          <td> 8503199</td>
          <td> 8913512.5</td>
          <td> 9383376</td>
        </tr>
        <tr>
          <th>School statutory low age</th>
          <td> 15615</td>
          <td>       4.009478</td>
          <td>       1.105218</td>
          <td>       2</td>
          <td>       3.0</td>
          <td>       4</td>
          <td>       5.0</td>
          <td>       8</td>
        </tr>
        <tr>
          <th>School statutory high age</th>
          <td> 15615</td>
          <td>      10.573999</td>
          <td>       1.169842</td>
          <td>       7</td>
          <td>      11.0</td>
          <td>      11</td>
          <td>      11.0</td>
          <td>      11</td>
        </tr>
      </tbody>
    </table>
    </div>



DEA on primary schools
----------------------

The DEA library does not yet account for exogenous characteristics. That
is partially accounted for by using only value-added measures as
outputs.

Metadata for all of the fields in the dataset is
`here <http://www.education.gov.uk/schools/performance/metadata.html>`__.

| Inputs: - Teaching Staff (£ per pupil) - Supply Teachers (£ per pupil)
| - Education Support Staff (£ per pupil)
| - Premises (incl. Staff costs) (£ per pupil)
| - Back Office (incl. Staff) (£ per pupil)
| - Catering (incl. Staff costs) (£ per pupil)
| - Other Staff Costs (£ per pupil)
| - Energy (£ per pupil) - Learning Resources (not ICT) (£ per pupil)
| - ICT Learning Resources (£ per pupil) - Bought in Professional
  Services (£ per pupil)
| - Other expenditure (£ per pupil)

Outputs: - MVAMEAS - RVAMEAS - WVAMEAS

Mung the data
~~~~~~~~~~~~~

Cut out the potential input and output columns. Drop anything with a
``np.NaN`` value. This will under-sample the data but should be enough
to test the DEA algorithm against real data.

.. code:: ipython3

    input_cols = [u'E01 Teaching Staff', u'E02 \nSupply teaching staff', u'E03 Education support staff', u'E04 Premises staff', u'E05 Administrative and clerical staff', u'E06 Catering staff', u'E07 \nCost of other staff', u'E08 Indirect employee expenses', u'E09 Development and training', u'E10 \nSupply teacher insurance', u'E11 \nStaff related insurance', u'E12 \nBuilding maintenance and improvement', u'E13 \nGrounds maintenance and improvement', u'E14 Cleaning and caretaking', u'E15 \nWater and sewerage', u'E16 \nEnergy', u'E17 \nRates', u'E18 \nOther occupation costs', u'E19 Learning resources (not ICT equipment)', u'E20 \nICT learning resources', u'E21 \nExam fees', u'E22 Administrative supplies', u'E23 \nOther insurance premiums', u'E24 Special facilities ', u'E25 Catering supplies', u'E26 Agency supply teaching staff', u'E27 \nBought in professional services – curriculum', u'E28 \nBought in professional services – other', u'E29 \nLoan interest', u'E31 Community focused school staff', u'E32 Community focused school costs']
    output_cols = ['MVAMEAS', 'RVAMEAS', 'WVAMEAS', ]
    inoutdat = primdat[input_cols + output_cols].dropna(how='any')
    inoutdat.describe().T[:5]




.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>count</th>
          <th>mean</th>
          <th>std</th>
          <th>min</th>
          <th>25%</th>
          <th>50%</th>
          <th>75%</th>
          <th>max</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>E01 Teaching Staff</th>
          <td> 433</td>
          <td> 1141533.493349</td>
          <td> 332241.644281</td>
          <td> 315772.00</td>
          <td> 883873.57</td>
          <td> 1106585.31</td>
          <td> 1326774.67</td>
          <td> 2438926.83</td>
        </tr>
        <tr>
          <th>E02 \nSupply teaching staff</th>
          <td> 433</td>
          <td>   16601.393487</td>
          <td>  24743.625269</td>
          <td>      0.00</td>
          <td>      0.00</td>
          <td>    7232.29</td>
          <td>   23247.65</td>
          <td>  169148.44</td>
        </tr>
        <tr>
          <th>E03 Education support staff</th>
          <td> 433</td>
          <td>  445495.999538</td>
          <td> 168205.591156</td>
          <td>  45273.94</td>
          <td> 321296.67</td>
          <td>  423777.00</td>
          <td>  540089.27</td>
          <td> 1105842.53</td>
        </tr>
        <tr>
          <th>E04 Premises staff</th>
          <td> 433</td>
          <td>   68796.045081</td>
          <td>  35941.585199</td>
          <td>      0.00</td>
          <td>  56192.62</td>
          <td>   68928.79</td>
          <td>   86875.40</td>
          <td>  293417.51</td>
        </tr>
        <tr>
          <th>E05 Administrative and clerical staff</th>
          <td> 433</td>
          <td>  107922.853926</td>
          <td>  46339.829420</td>
          <td>      0.00</td>
          <td>  79439.68</td>
          <td>   98027.43</td>
          <td>  125055.44</td>
          <td>  466979.23</td>
        </tr>
      </tbody>
    </table>
    </div>



*Why are there so few schools left after dropping missing data? Must be
some common exclusion causing too many to be dropped.*

Check distribution of the data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: ipython3

    import math
    
    sns.set_style("white")
    
    num_plots = len(input_cols)
    n = int(math.ceil(math.sqrt(num_plots)))
    
    fig = plt.figure(figsize=(20, 20))
    axes = [plt.subplot(n, n, i) for i in range(1, num_plots + 1)]
    
    i = 0
    for k, v in inoutdat[input_cols].iteritems():
        ax = axes[i]
        sns.kdeplot(v, shade=True, ax=ax, legend=False)
        [label.set_visible(False) for label in ax.get_yticklabels()]
        ax.xaxis.set_ticks([v.min(), v.max()])
        ax.set_title(k)
        i += 1
    sns.despine(left=True, trim=True, fig=fig)
    plt.tight_layout()



.. image:: DEA%20of%20English%20schools_files/DEA%20of%20English%20schools_16_0.png


Correlation between inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^

There are too many inputs so check for highly correlated inputs and drop
them.

.. code:: ipython3

    sns.set()
    with sns.plotting_context(rc={"figure.figsize": (25, 25),
                                  "axis.labelsize": 6}):
        sns.corrplot(inoutdat[input_cols])



.. image:: DEA%20of%20English%20schools_files/DEA%20of%20English%20schools_18_0.png


Correlations don’t appear to be strong so this isn’t going to be a
productive strategy. Can I drop inputs that have a very low value?

Sort inputs by size
^^^^^^^^^^^^^^^^^^^

.. code:: ipython3

    med = inoutdat[input_cols].median()
    med.sort(ascending=False)
    with sns.plotting_context(rc={"figure.figsize": (15, 6)}):
        sns.violinplot(inoutdat[med.index], color="coolwarm_r")
    plt.xlabel("Expenditure")
    plt.title("Distribution of expenditure by category")
    sns.despine()



.. image:: DEA%20of%20English%20schools_files/DEA%20of%20English%20schools_21_0.png


Clearly not many of these costs are significant. Picking the top five:

.. code:: ipython3

    med.index[:5].values




.. parsed-literal::

    array(['E01 Teaching Staff', 'E03 Education support staff',
           'E05 Administrative and clerical staff',
           'E19 Learning resources (not ICT equipment)',
           'E25 Catering supplies'], dtype=object)



.. code:: ipython3

    totin = inoutdat[input_cols].sum().sum()
    inoutdat[med.index[:5].values].sum().div(totin)




.. parsed-literal::

    E01 Teaching Staff                            0.450038
    E03 Education support staff                   0.175632
    E05 Administrative and clerical staff         0.042547
    E19 Learning resources (not ICT equipment)    0.038280
    E25 Catering supplies                         0.029932
    dtype: float64



.. code:: ipython3

    inoutdat[med.index[:5].values].sum().div(totin).cumsum()




.. parsed-literal::

    E01 Teaching Staff                            0.450038
    E03 Education support staff                   0.625670
    E05 Administrative and clerical staff         0.668218
    E19 Learning resources (not ICT equipment)    0.706498
    E25 Catering supplies                         0.736430
    dtype: float64



The top five account for less the three-quarters of the total
expenditure so this isn’t ideal. It might be worth trying a PCA approach
later by way of comparison.

Set up and solve the DEA problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    %%time
    primDEA = dea.DEAProblem(inoutdat[med.index[:5]], inoutdat[output_cols], returns='CRS')


.. parsed-literal::

    Wall time: 3min 35s


.. code:: ipython3

    %%time
    primResults = primDEA.solve()


.. parsed-literal::

    Wall time: 2min 56s


.. code:: ipython3

    primResults['Efficiency'].hist(bins=50)




.. parsed-literal::

    <matplotlib.axes.AxesSubplot at 0x4280bcf8>




.. image:: DEA%20of%20English%20schools_files/DEA%20of%20English%20schools_30_1.png


That’s a good spread but the inputs are very limited. Could we use PCA
to limit them instead of truncating at the biggest five?

PCA analysis of the inputs and outputs
--------------------------------------

Aim for components that explain at least 80 per cent of the variation in
the target variables. Jollife (1972) also suggest only using components
with eigenvalues greater than 0.7.

.. code:: ipython3

    indat_pca = dea.tools.deaPCA(inoutdat[input_cols])



.. image:: DEA%20of%20English%20schools_files/DEA%20of%20English%20schools_32_0.png


.. code:: ipython3

    outdat_pca = dea.tools.deaPCA(inoutdat[output_cols])



.. image:: DEA%20of%20English%20schools_files/DEA%20of%20English%20schools_33_0.png


.. code:: ipython3

    plt.scatter(indat_pca[0].values, outdat_pca[0].values)




.. parsed-literal::

    <matplotlib.collections.PathCollection at 0x42683b00>




.. image:: DEA%20of%20English%20schools_files/DEA%20of%20English%20schools_34_1.png


.. code:: ipython3

    %%time
    pcaDEA = dea.DEAProblem(indat_pca.iloc[:,:2], outdat_pca.iloc[:,:2], returns='CRS')


.. parsed-literal::

    Wall time: 2min 11s


.. code:: ipython3

    %%time
    pcaResults = pcaDEA.solve()


.. parsed-literal::

    Wall time: 2min 43s


.. code:: ipython3

    fig1, ax1 = plt.subplots()
    pcaResults['Efficiency'].hist(bins=50, ax=ax1, alpha=0.4)
    primResults['Efficiency'].hist(bins=50, ax=ax1, alpha=0.2)
    plt.legend(['PCA', 'Raw'])




.. parsed-literal::

    <matplotlib.legend.Legend at 0x5d57e780>




.. image:: DEA%20of%20English%20schools_files/DEA%20of%20English%20schools_37_1.png


There doesn’t seem to be any good reason to prefer
