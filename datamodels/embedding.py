""" datamodels.embedding.py
`Embedding` class skeleton interface
"""
from abc import ABC, abstractmethod


class Embedding(ABC):
    """Embedding datamodel
    args:
        name (str): Embedding name
        type (str): Embedding type (example: node2vec, word2vec)
        description (str): embedding description
    """

    def __init__(self, name=None, type=None, description=None):
        self.name = name
        self.type = type
        self.description = description

    @abstractmethod
    def from_networkx_graph(self):
        raise NotImplementedError

    @abstractmethod
    def optimize_hyperparameters(self):
        raise NotImplementedError
