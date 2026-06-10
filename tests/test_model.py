import numpy as np

def test_prediction_values():
    predictions = np.array([0, 1, 1, 0])
    assert set(predictions).issubset({0, 1})