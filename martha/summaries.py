import pandas as pd
import sys
import hurry.filesize
from collections import Counter

def distribution(column):
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
    totalValues = column.count()
    dist = pd.DataFrame(pd.Series(Counter(column), name = "occurences"))
    dist = dist.assign(percent = round(dist.occurences / totalValues * 100, 2))
    dist = dist.sort_values("percent", ascending = False)
    return dist

def IQR(column):
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
    interquartileRange = column.quantile(0.75) - column.quantile(0.25)
    return interquartileRange


def countColumn(data):
    try:
        topValue = pd.Series(data.value_counts(sort = True, ascending = False))
        return topValue.index[0]
    except Exception as err:
        return "NA"

def columnStats(data):
    '''
    Column Stats Summary
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
        .assign(missingPercent = round(typeData.missingValues / totalRows * 100, 2))
        .assign(uniquePercent = round(typeData.uniqueValues / totalRows * 100, 2))
    )

    typeData = (
        typeData
        .assign(topRecurringValues = data.apply(lambda x: countColumn(x), axis = 0))
    )
    return typeData


def countTypes(data):
    '''
    Use as part of summary()
    '''
    dataTypes = ['int32', 'int64', 'object', 'datetime64[ns]']
    data = pd.DataFrame(data.dtypes, columns = ['type'])
    int32s = len(data[data['type'] == dataTypes[0]])
    int64s = len(data[data['type'] == dataTypes[1]])
    ints = int32s + int64s
    objects = len(data[data['type'] == dataTypes[2]])
    datetimes = len(data[data['type'] == dataTypes[3]])
    return ints, objects, datetimes

def summary(data):
    '''
    Data Stats Summary
    Data Stats Summary is used to provide some informatiom about the quality
    of a dataset. This includes showing information such as:
     : The data type of each column
    totalRows : The total number of rows
    totalColumns : The total number of columns
    totalTypes : The total number of various data types
    totalSize : the size in MB, KB etc of the dataset
    totalMissing : Total number of missing values in all columns
    totalMissingPercent : Total number of missing values in all columns percentage
    ------
    PARAMS
    ------
    data : The dataset you want to summarize
    '''
    totalRows = pd.Series(len(data), name = "Total Number of Rows", index = ["metric"])
    totalColumns = pd.Series(len(data.columns), name = 'Total Number of Columns', index = ["metric"])
    totalTypes = countTypes(data)

    totalInts = pd.Series(totalTypes[0], name = "Numeric", index = ['metric'])
    totalStrings = pd.Series(totalTypes[1], name = "String", index = ['metric'])
    totalDates = pd.Series(totalTypes[2], name = "Date", index = ['metric'])

    totalSize = pd.Series(hurry.filesize.size(sys.getsizeof(data)), name = "Total Size in Memory", index = ["metric"])
    totalMissing = data.apply(lambda x: x.isnull().sum(), axis = 0).sum()
    totalMissingPercent = pd.Series(str(int(totalMissing / (totalRows * totalColumns) * 100)) + "%", name = "Total Missing %", index = ['metric'])

    allStats = pd.DataFrame()
    stats = [totalRows, totalColumns, totalInts, totalStrings, totalDates, totalSize, totalMissingPercent]

    for stat in stats:
        allStats = allStats.append(stat)
    return allStats

def showNullColumns(data, threshold = 0):
    '''
    showNullColumns
    This will return all the columns in a dataset that have nulls passed
    a given threshold.
    ------
    PARAMS
    ------
    data : that contains the column you're interested in checking
    threshold : Return all columsn with null counts greater than this value. Default is 0.
    '''
    nullColumns = pd.DataFrame(data.isnull().sum()[data.isnull().sum() > threshold])
    return nullColumns
