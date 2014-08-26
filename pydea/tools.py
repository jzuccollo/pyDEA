# Tools for working with the solved DEA objects.


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
    
    import statsmodels.api as sm
    from statsmodels.formula.api import logit
    
    corr_data = env_vars.join(dea_obj.results['Efficiency'])
    corr_mod = logit("Efficiency ~ " + " + ".join(env_vars.columns), corr_data).fit()
    
    mfx = corr_mod.get_margeff()
    print mfx.summary()
    
    return corr_mod


def deaPCA(df):
    """
    Extract principal components from pandas dataframe and shift distribution so that all values are strictly positive, as required for DEA.
    """
    
    from sklearn.decomposition import PCA as sklearnPCA

    indat_pca = sklearnPCA()
    indat_transf = pd.DataFrame(indat_pca.fit_transform(df.values), index=df.index)

    for ser, vals in indat_transf.iteritems():
        if vals.min() <=0:
            indat_transf[ser] = vals + np.abs(vals.min()) + 1
   
    fig1, ax1 = plt.subplots()
    ax1.plot(np.array(indat_pca.explained_variance_ratio_).cumsum())
    ax1.bar(np.arange(0.1, len(indat_pca.explained_variance_ratio_), 1), np.array(indat_pca.explained_variance_ratio_))
    ax1.set_title('Variance explained by each principal component')
    ax1.set_xlim(right=len(indat_pca.explained_variance_ratio_))
    ax1.set_ylim(top=1)
    
    return indat_transf