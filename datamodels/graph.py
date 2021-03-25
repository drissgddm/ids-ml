""" datamodels.graph.py
`Graph` class skeleton interface
"""
from abc import ABC, abstractmethod


class Graph(ABC):
    """Graph datamodel
    args:
        name (str): graph name
        type (str): graph type (example: unigraph, multigraph)
        description (str): graph description
    """

    def __init__(self, name=None, type=None, description=None):
        self.name = name
        self.type = type
        self.description = description

    @abstractmethod
    def add_nodes(self):
        raise NotImplementedError

    @abstractmethod
    def add_edges(self):
        raise NotImplementedError

    @abstractmethod
    def plot(self):
        raise NotImplementedError
