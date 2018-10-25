import pandas as pd
import numpy as np
import sys
import warnings
try:
    import altair as alt
except ImportError:
    warnings.warn("Altair is not installed. Chart functions won't work")

def showNullRows(data, column):
    return data[[column].isnull()]

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

def numericHistograms(data):
    """
    Generate a chart for all numeric values in Pandas DataFrame

    For all the numeric columns in a Pandas Dataframe, this function
    will generate a Histogram to show how the data is distributed

    Attributes
    ----------
    data : pd.DataFrame, default None
    A Pandas DataFrame that contains numeric values
    """
    numericColumns = data.select_dtypes(np.number)
    columns = numericColumns.columns.tolist()

    chart = alt.Chart(data, height = 100).mark_bar().encode(
            x = alt.X(alt.repeat('row'), type='quantitative', bin = True),
            y = alt.Y("count()", type='quantitative')
    ).repeat(
        row = columns
    )
    return chart

def missingDates(data, freq = "D", format = '%Y-%m-%d', returnType = "viz"):
    """
    Check for Missing Dates

    This function is used to return either a list of missing dates from a pd.Series or
    chart the missing dates.

    Attributes
    ----------
    data : pd.Series, default None
    A Pandas series that contains dates. Dates will be parsed using pd.to_datetime()
    with a default strftime of '%Y-%m-%d'. Use strftime arg to alter date format
    freq: object, default '%Y-%m-%d'
    The expected frequency of the dates. Valid options are:
        B: business day frequency
        C: custom business day frequency
        D: calendar day frequency
        W: weekly frequency
        M: month end frequency
        SM: semi-month end frequency (15th and end of month)
        BM: business month end frequency
        CBM: custom business month end frequency
        MS: month start frequency
        SMS: semi-month start frequency (1st and 15th)
        BMS: business month start frequency
        CBMS: custom business month start frequency
        Q: quarter end frequency
        BQ: business quarter end frequency
        QS: quarter start frequency
        BQS: business quarter start frequency
        A, Y: year end frequency
        BA, BY: business year end frequency
        AS, YS: year start frequency
        BAS, BYS: business year start frequency
        BH: business hour frequency
        H: hourly frequency
        T, min: minutely frequency
        S: secondly frequency
        L, ms: milliseconds
        U, us: microseconds
        N: nanoseconds
    format:
    returnType: object, default viz
    One of:
        missing: Return the missing dates
        all: Return missing and present dates
        viz: Return a vizualisation
    """
    try:
        assert type(data) == pd.Series

        datesToCheck = pd.to_datetime(list(data))

        minDate = datesToCheck.min().strftime("%Y-%m-%d")
        maxDate = datesToCheck.max().strftime("%Y-%m-%d")
        computedRange = pd.date_range(minDate, maxDate, freq = freq)

        allChecks = []
        for date in computedRange:
            currentDateResult = date in datesToCheck
            currentDate = {"date" : date, "exists" : currentDateResult}
            allChecks.append(currentDate)

        allChecks = pd.DataFrame(allChecks)
        missing = list(allChecks.exists).count(False)
        present = list(allChecks.exists).count(True)
        total = present + missing

        allChecks['date'] = allChecks.date.map(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d'))

        calculatedTitle = "Total Dates: " + str(total) + ", Missing Dates: " + str(missing) + ", (" + str(int((missing / total) * 100)) + "%)"

        scale = alt.Scale(domain=['true', 'false'],
                          range=['#B8E986', '#F15545'])

        if returnType == 'viz':
            xRange = len(computedRange)
            barSize = (800 / xRange)
            padding = (barSize / 2) + 1

            results = alt.Chart(
                allChecks,
                title = alt.TitleParams(calculatedTitle, anchor = "start", offset = 20, orient = "top"),
                width = 800,
                height = 400,
                autosize = alt.AutoSizeParams(
                    contains="content",
                    resize=True,
                    type="fit")
                ).mark_bar(size = barSize).encode(
                    x = alt.X("date",axis = alt.Axis(tickCount = xRange), title = "Date", type = "temporal", scale=alt.Scale(padding = padding)),
                    y = "count()",
                    color = alt.Color("exists", scale = scale),
                    tooltip = [alt.Tooltip("date", format = "%Y-%m-%d", type = "temporal"), "exists", "count()"]
                ).interactive(
                    bind_y = False)

        elif returnType == "missing":
            results = allChecks[allChecks['exists'] == False]
        elif returnType == "all":
            results = allChecks
        return results
    except Exception as E:
        raise E
