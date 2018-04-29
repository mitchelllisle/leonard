import pandas as pd
from sklearn.preprocessing import LabelEncoder

def negabs(x):
    '''
    Inverse of ABS

    This is a simple functions for turning a positive number
    into a negative numbers.
    ----------
    PARAMS
    ----------
    x : Number to turn into a negative number

    ----------
    EXAMPLE
    ----------
    df.assign(negativeY = df.y.apply(lambda x: negabs(x)))
    '''
    return x * -1


def normalise(data):
    '''
    Normalise a list of values to a number between 0 and 1

    This is a simple functions for turning a sequence of numbers
    into a value between 0 and 1. Useful for machine learning
    algorithms that require all features being on the same scale.
    ----------
    PARAMS
    ----------
    data : Column to apply normalise function over
    ----------
    EXAMPLE
    ----------
    data.assign(score = normalise(data, 'ProductionBudget'))
    '''
    minVal = data.min()
    maxVal = data.max()
    normalisedVals = (data - minVal) / (maxVal - minVal)
    return normalisedVals


def labelEncoder(data, column):
    '''
    labelEncoder
    Simple function for making Sklearn LabelEncoder easier to use in
    data science workflow. Given a string column, it will return integer
    encoded values for use in a machine learning algorithm that expects
    numeric values.
    ------
    PARAMS
    ------
    data : that contains the column you're interested in encoding
    column : Column that is to be encoded

    -------
    EXAMPLE
    -------
    fifaAbilities.assign(preferred_foot = mh.labelEncoder(fifaAbilities, "preferred_foot"))
    '''
    values = list(data[column])
    encodedLabels = LabelEncoder()
    encodedLabels = encodedLabels.fit_transform(values)
    return encodedLabels
