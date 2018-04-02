import pytest
from leonard import distribution
from leonard import IQR
import numpy as np
import pandas as pd
import json

# Test Definitions
def test_distribution():
    values = pd.DataFrame(pd.Series(["Orange","Apple","Banana","Orange","Banana","Banana","Banana","Grapes","Apple","Banana","Apple"]), columns = ["Fruits"])
    
    distResult = distribution(values, "Fruits")
    
    topFruit = distResult.iloc[0]['Fruits']
    assert topFruit == 'Banana'    
    
def test_IQR():
    values = pd.DataFrame(pd.Series([3,5,52,45,53,56,97,23,45,81,63]), columns = ["ranges"])
    
    result = IQR(values, "ranges")
    
    assert result == 25.5
    

# Run Functions
test_distribution()
test_IQR()
