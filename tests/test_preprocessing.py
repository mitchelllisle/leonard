import pytest
from martha import negabs
from martha import normalise
from martha import labelEncoder
from martha import cleanUpString
from martha import medianFrequency
from martha import gini
import numpy as np
import pandas as pd
import json
from sklearn.preprocessing import LabelEncoder

# import os
# os.chdir("/Users/mitchell/Documents/projects/martha")

def test_negabs():
    data = pd.read_csv("data/marvelMovies.csv")

    result = data.assign(ProductionBudget = data.ProductionBudget.apply(lambda x: negabs(x)))
    result = result.ProductionBudget.apply(lambda x: x < 0)

    assert any(result) == True

def test_normalise():
    data = pd.read_csv("data/marvelMovies.csv")
    result = data.assign(score = normalise(data['ProductionBudget']))
    assert 'score' in result.columns

def test_labelEncoder():
    data = pd.read_csv("data/fifaAbilities.csv")
    result = data.assign(preferred_foot_encoded = labelEncoder(data, "preferred_foot"))
    assert result.preferred_foot_encoded.dtype == 'int64'

def test_cleanUpString():
    data = "test, \n"
    result = cleanUpString(data, strip_chars = [','], replace_extras = {"t" : "--"})
    assert result == '--es--'

def test_medianFrequency():
    data = {"values" : [1,2,4], "repeats" : [4,4,2]}
    values = pd.Series(data['values'])
    repeats = pd.Series(data['repeats'])
    computedMedian = medianFrequency(values, repeats)
    assert computedMedian == 2

def test_gini():
    data = pd.read_csv("data/fifaAbilities.csv")
    assert gini(data['marking']) == 0.3441157017683561
