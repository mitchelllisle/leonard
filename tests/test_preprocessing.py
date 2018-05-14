import pytest
from martha import negabs
from martha import normalise
from martha import labelEncoder
from martha import cleanUpString
import numpy as np
import pandas as pd
import json
from sklearn.preprocessing import LabelEncoder

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
    result = cleanUpString(data, strip_chars = [','])
    assert result == 'test'
