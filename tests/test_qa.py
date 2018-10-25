import pytest
from martha import missingDates
from martha import numericHistograms
from martha import showNullColumns
try:
    import altair as alt
except ImportError:
    warnings.warn("Altair is not installed. Chart functions won't work")
import numpy as np
import pandas as pd
import json

def test_checkMissingDates_1():
    dates = pd.Series(['2017-01-01', '2017-01-02', '2017-01-04', '2017-01-06'], name = "dates")
    datesFound = missingDates(dates, returnType = 'missing')
    allDates = missingDates(dates, returnType = 'all')
    assert len(datesFound == 2)
    assert len(allDates == 6)

def test_checkMissingDates_2():
    dates = pd.Series(['2017-01-01', '2017-01-02', '2017-01-04', '2017-01-06'], name = "dates")
    datesFound = missingDates(dates, returnType = 'viz')
    assert type(datesFound) == alt.Chart

def test_numericColumns():
    data  = pd.read_csv("data/fifaAbilities.csv")
    charts = numericHistograms(data)
    assert type(charts) == alt.RepeatChart

def test_showNullColumns():
    data = pd.read_csv("data/marvelMovies.csv")
    result = showNullColumns(data)
    assert len(result) == 1
