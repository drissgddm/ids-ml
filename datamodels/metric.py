""" datamodels.metric.py
`Metric` class skeleton interface
"""
from abc import ABC, abstractmethod


class Metric(ABC):
    """Metric datamodel
    args:
        name (str): metric name
        type (str): type name (example: rmse, r2)
        description (str): metric description
    """

    def __init__(self, name=None, type=None, description=None):
        self.name = name
        self.type = type
        self.description = description

    @abstractmethod
    def evaluate(self):
        """Compute metric evaluation
        :returns: result
        """
        raise NotImplementedError

    @abstractmethod
    def plot(self):
        """Plot the evaluation result in a eloquent graph
        :returns: the graph displayed
        """
        raise NotImplementedError
