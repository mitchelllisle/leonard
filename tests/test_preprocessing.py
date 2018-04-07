import pytest
from martha import negabs
import numpy as np
import pandas as pd
import json

def test_negabs():
    data = pd.read_csv("data/marvelMovies.csv")
    
    result = data.assign(ProductionBudget = data.ProductionBudget.apply(lambda x: negabs(x)))
    result = result.ProductionBudget.apply(lambda x: x < 0)
    
    assert any(result) == True