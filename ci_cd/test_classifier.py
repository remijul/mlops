# test_classifier.py
import pytest
from classifier import load_data, train_model

def test_load_data():
    X, y = load_data()
    assert X.shape == (150, 4)
    assert y.shape == (150,)

def test_train_model():
    X, y = load_data()
    model, accuracy = train_model(X, y)
    assert accuracy > 0.95 #Error with > 2   #OK with 0.8

if __name__ == "__main__":
    pytest.main()
