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
    
    --------
    EXAMPLES
    --------
    Coming soon......
    '''
    dist = (
        data
        .groupby(column)
        .agg({column : "count"})
        .rename(columns = {column : "Count"})
        .sort_values("Count", ascending = False).reset_index()
    )

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