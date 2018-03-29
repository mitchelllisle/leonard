import pytest
from leonard import summaries
import numpy as np
import pandas as pd
import json

# Test Definitions
def test_ditribution():
    values = pd.DataFrame(pd.Series(["Orange","Apple","Banana","Orange","Banana","Banana","Banana","Grapes","Apple","Banana","Apple"]), columns = ["Fruits"])
    
    distResult = distribution(values, "Fruits")
    
    topFruit = distResult.iloc[0]['Fruits']
    assert topFruit == 'Banana'    
    

# Run Functions
test_ditribution()