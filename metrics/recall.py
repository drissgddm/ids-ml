""" metrics.recall.py
Model class: Recall
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html
"""
from datamodels.metric import Metric

from sklearn.metrics import recall_score


class Recall(Metric):
    """Recall Metric class
    Compute the recall.
    The recall is the ratio tp / (tp + fn) where tp is the number of
     true positives and fn the number of false negatives.
    The recall is intuitively the ability
     of the classifier to find all the positive samples.
    The best value is 1 and the worst value is 0.
    """

    def __init__(self):
        super().__init__(name="Recall", type="Multiclassification Evaluation")

    def evaluate(self, Y_true, Y_predicted, average="micro"):
        """Compute the accuracy score
        :returns: a float
        """
        return recall_score(Y_true, Y_predicted, average=average)

    def plot(self, Y_true, Y_predicted, normalize="true", labels=None):
        pass
