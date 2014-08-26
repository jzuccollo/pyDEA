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