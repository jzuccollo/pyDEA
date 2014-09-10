# Tools for working with the solved DEA objects.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def env_corr(dea_obj, env_vars):
    """
    Determine correlations with environmental/non-discretionary variables using a logit regression. Tobit will be implemented when available upstream in statsmodels.

    Takes:
        dea_obj: The solved DEA instance.
        env_vars: A pandas dataframe of

    Returns:
        corr_mod: the statsmodels' model instance containing the inputs and results from the logit model.

    Note that there can be no spaces in the variables' names.
    """

    print "A logit regression will be used. A censored regression with a Tobit model would be more correct but it is not yet provided by statsmodels.\n"

    from statsmodels.formula.api import logit

    corr_data = env_vars.join(dea_obj.results['Efficiency'])
    corr_mod = logit(
        "Efficiency ~ " + " + ".join(env_vars.columns), corr_data).fit()

    mfx = corr_mod.get_margeff()
    print mfx.summary()

    return corr_mod


def normalise_df(df):
    """
    Normalise the series in a dataframe to z-scores,

    """

    dfnorm = pd.DataFrame(index=df.index)
    for ind, ser in df.iteritems():
        dfnorm[ind] = (ser - ser.mean()) / ser.std()
    return dfnorm


def deaPCA(df, allres=False, normalise=False, plot=True):
    """
    Extract principal components from pandas dataframe and shift distribution so that all values are strictly positive, as required for DEA.

    Takes:
        df: A dataframe of series to run the PCA on.
        allres: Boolean. Set True if you would like to get the PCA object returned instead of the transformed data. This can be useful if you wish to use the entire results of the PCA.
        normalise: Boolean. Set True to normalise the series to a z-score before transforming.
        plot: Should the function display a plot of the variance explained?
    """

    from sklearn.decomposition import PCA as sklearnPCA

    if normalise:
        df = normalise_df(df)

    indat_pca = sklearnPCA()
    indat_transf = pd.DataFrame(
        indat_pca.fit_transform(df.values), index=df.index)

    for ser, vals in indat_transf.iteritems():
        if vals.min() <= 0:
            indat_transf[ser] = vals + np.abs(vals.min()) + 1

    if plot:
        _, ax1 = plt.subplots()
        ax1.plot(np.array(indat_pca.explained_variance_ratio_).cumsum())
        ax1.bar(np.arange(0.1, len(indat_pca.explained_variance_ratio_), 1), np.array(
            indat_pca.explained_variance_ratio_))
        ax1.set_title('Variance explained by each principal component')
        ax1.set_xlim(right=len(indat_pca.explained_variance_ratio_))
        ax1.set_ylim(top=1)

    if allres:
        return indat_pca
    else:
        return indat_transf
