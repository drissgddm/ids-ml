""" datamodels.dim_reducer.py
`DimensionsReducer` class skeleton interface
"""
from abc import ABC, abstractmethod


class DimensionsReducer(ABC):
    """DimensionReducer datamodel
    args:
        name (str): Dimension reducer name
        type (str): Dimension reducer type (example: PCA, t-SNE, AutoEncoders)
        description (str): embedding description
    """

    def __init__(self, name=None, type=None, description=None):
        self.name = name
        self.type = type
        self.description = description

    @abstractmethod
    def fit(self):
        raise NotImplementedError

    @abstractmethod
    def plot(self):
        raise NotImplementedError
