import pandas as pd

def distribution(data, column):
    '''
    Distribution of data based off Categories in column
    
    This functions works off categorical data. It will return the frequency and percentage 
    of data points that fit to each distinct category.
    
    ------
    PARAMS
    ------
    data : that contains the column you're interested in checking
    column : the column to run distribution checks
    '''
    totalValues = data[column].count()
    dist = (
        data
        .groupby(column)
        .agg({column : "count"})
        .rename(columns = {column : "Count"})
        .sort_values("Count", ascending = False).reset_index()
    )
    
    dist = dist.assign(Percent = round(dist.Count / totalValues * 100, 2))
    return dist

def IQR(data, column):
    '''
    Interquartile Range (IQR)

    The interquartile range (IQR) is the range of the data that contains the middle 50% of cases. Recall that you find
    the range by subtracting the minimum value from the maximum value in the dataset. You calculate in the IQR in a
    simlar way, except that you find the difference between the 1st quartile (Q1) and the 3rd quartile (Q3)
    ------
    PARAMS
    ------
    data : that contains the column you're interested in checking
    column : the column to run distribution checks
    
    '''
    interquartileRange = data[column].quantile(0.75) - data[column].quantile(0.25)
    return interquartileRange


def columnStats(data):
    '''
    Column Stats Summary (IQR)

    Column Stats Summary is used to provide some informatiom about the quality 
    of each column in a dataset. This includes showing information such as:
    dataType : The data type of each column
    totalValues : The total number of values, not unique.
    uniqueValues : The total number of unique values
    missingValues : The total number of values that are NULL
    missingPercent : (missingValues / totalValues * 100)
    ------
    PARAMS
    ------
    data : that contains the column you're interested in checking
    '''
    totalRows = len(data)
    typeData = pd.DataFrame(data.dtypes, columns = ['dataTypes'])
    typeData = (
        typeData
        .assign(totalValues = data.apply(lambda x: x.count(), axis = 0))
        .assign(uniqueValues = data.apply(lambda x: x.nunique(), axis = 0))
        .assign(missingValues = data.apply(lambda x: x.isnull().sum(), axis = 0))
    )
    
    typeData = (
        typeData
        .assign(missingPercent = round(typeData.missingValues / rows * 100, 2))
        .assign(uniquePercent = round(typeData.uniqueValues / totalRows * 100, 2))
    )
    return typeData
