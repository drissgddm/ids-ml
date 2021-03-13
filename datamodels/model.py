""" datamodels.model.py
`Model` class skeleton interface
"""
from abc import ABC, abstractmethod


class Model(ABC):
    """Model model

    :params:
        name (str): model name
        type (str): type of algorithm (ex: arima, linear_regression...)
        hyperparameters_list (list): list of hyperparameters to input
        description (str): model description
    """

    def __init__(
        self, name=None, type=None, hyperparameters_list=None, description=None
    ):
        self.name = name
        self.type = type
        self.hyperparameters_list = hyperparameters_list
        self.description = description

    @abstractmethod
    def apply_preprocessing(self):
        """Apply preprocessing
        :return: data preprocessed
        """
        raise NotImplementedError

    @abstractmethod
    def train(self):
        """Train the model for the given data
        must fit the `model` property and return it
        """
        raise NotImplementedError

    @abstractmethod
    def predict(self):
        """Predict
        :return: predictions
        """
        raise NotImplementedError
