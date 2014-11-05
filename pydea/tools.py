# Tools for working with the solved DEA objects.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def _all_positive(df):
    """
    Ensure that all values in a dataframe are strictly positive by
    adding a constant.
    """

    dfpos = pd.DataFrame(index=df.index)
    for ser, vals in list(df.items()):
        if vals.min() <= 0:
            dfpos[ser] = vals + np.abs(vals.min()) + 1
    return dfpos


def normalise_df(df, all_positive=False):
    """
    Normalise the series in a dataframe to z-scores,

    """

    dfnorm = pd.DataFrame(index=df.index)
    for ind, ser in list(df.items()):
        dfnorm[ind] = (ser - ser.mean()) / ser.std()

    if all_positive:
         dfnorm = _all_positive(dfnorm)

    return dfnorm


def deaPCA(df, allres=False, normalise=False, plot=True):
    """
    Extract principal components from pandas dataframe and shift distribution
    so that all values are strictly positive, as required for DEA.

    Takes:
        df: A dataframe of series to run the PCA on.
        allres: Boolean. Set True if you would like to get the PCA object
                returned instead of the transformed data. This can be
                useful if you wish to use the entire results of the PCA.
                The object is a fit_transformed sklearn.decomposition.PCA
                object.
        normalise: Boolean. Set True to normalise the series to a z-score
                before transforming.
        plot: Should the function display a plot of the variance explained?
    """

    from sklearn.decomposition import PCA as sklearnPCA

    if normalise:
        df = normalise_df(df)

    indat_pca = sklearnPCA()
    indat_transf = pd.DataFrame(
        indat_pca.fit_transform(df.values), index=df.index)

    pca_colnames = ["PCA" + str(i) for i in indat_transf.columns]
    indat_transf.columns = pca_colnames

    indat_transf_pos = _all_positive(indat_transf)

    if plot:
        _, ax1 = plt.subplots()
        ax1.plot(np.array(indat_pca.explained_variance_ratio_).cumsum())
        ax1.bar(np.arange(0.1, len(indat_pca.explained_variance_ratio_), 1),
                np.array(indat_pca.explained_variance_ratio_))
        ax1.legend(['Cumulative variance explained',
            'Variance explained by component'], loc='center right')
        ax1.set_ylabel('Proportion of variance explained')
        ax1.set_title('Variance explained by each principal component')
        ax1.set_xlim(right=len(indat_pca.explained_variance_ratio_))
        ax1.set_ylim(top=1)

    if allres:
        return indat_pca
    else:
        return indat_transf_pos
