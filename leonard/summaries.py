def distribution(data, column):
    '''
    Distribution of data based off Categories in column
    
    @description This functions works off categorical data. It 
    will return the frequency and percentage of data points that fit to each distinct category.
    
    @param data that contains the column you're interested in checking
    @param column the column to run distribution checks
    '''
    dist = (
        data
        .groupby(column)
        .agg({column : "count"})
        .rename(columns = {column : "Count"})
        .sort_values("Count", ascending = False).reset_index()
    )

    return dist