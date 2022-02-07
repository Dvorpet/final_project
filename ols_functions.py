import statsmodels.api as sm

def simplemodel(df):
    result = sm.OLS(df['price'], sm.add_constant(df.loc[:,df.columns != 'price'])).fit()
    return result.summary()

def modelparameters(df):
    result = sm.OLS(df['price'], sm.add_constant(df.loc[:,df.columns != 'price'])).fit()
    return result.params
    