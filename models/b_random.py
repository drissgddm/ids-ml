""" models.b_random.py
Model class: RandomBaseline
"""
from datamodels.metric import Model

from random import randint


class RandomBaseline(Model):
    def __init__(self):
        super().__init__(
            name="Random Baseline", type="Random"
        )

    def apply_preprocessing(self):
        pass

    def train(self):
        pass

    def predict(self, X):
        return [randint(0, 4) for _ in range(len(X))]
