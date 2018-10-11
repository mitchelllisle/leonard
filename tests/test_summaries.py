import pytest
from martha import distribution
from martha import IQR
from martha import columnStats
from martha import summary
from martha import showNullColumns
try:
    import altair as alt
except ImportError:
    warnings.warn("Altair is not installed. Chart functions won't work")
import numpy as np
import pandas as pd
import json

# Test Definitions
def test_distribution():
    values = pd.DataFrame(pd.Series(["Orange","Apple","Banana","Orange","Banana","Banana","Banana","Grapes","Apple","Banana","Apple"]), columns = ["Fruits"])
    distResult = distribution(values["Fruits"])
    topFruit = distResult['index'][0]
    assert topFruit == 'Banana'

def test_IQR():
    values = pd.DataFrame(pd.Series([3,5,52,45,53,56,97,23,45,81,63]), columns = ["ranges"])

    result = IQR(values["ranges"])

    assert result == 25.5


def test_columnStats():
    data = pd.read_csv("data/marvelMovies.csv")

    result = columnStats(data)

    assert len(result.columns) == 7


def test_summary():
    data = pd.read_csv("data/marvelMovies.csv")

    result = summary(data)

    assert len(result) == 7

def test_showNullColumns():
    data = pd.read_csv("data/marvelMovies.csv")

    result = showNullColumns(data)

    assert len(result) == 1
