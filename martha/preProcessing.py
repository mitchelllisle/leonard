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