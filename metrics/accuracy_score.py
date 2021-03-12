""" metrics.accuracy_score.py
Model class: AccuracyScore
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
"""
from datamodels.metric import Metric

from sklearn.metrics import accuracy_score


class AccuracyScore(Metric):
    """Accuracy Score Metric class
    Compute the accuracy classification score
    """

    def __init__(self):
        super().__init__(
            name="Accuracy Score", type="Multiclassification Evaluation"
        )

    def evaluate(self, Y_true, Y_predicted, normalize="true"):
        """Compute the accuracy score
        :returns: a float
        """
        return accuracy_score(Y_true, Y_predicted, normalize=normalize)

    def plot(self, Y_true, Y_predicted, normalize="true", labels=None):
        pass
