import pandas as pd

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
