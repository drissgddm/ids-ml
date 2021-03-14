""" metrics.confusion_matrix.py
Model class: ConfusionMatrix
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
"""
from datamodels.metric import Metric

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from seaborn import heatmap


class ConfusionMatrix(Metric):
    """Confusion Matrix Metric class
    Compute the confusion matrix
    """

    def __init__(self):
        super().__init__(name="Confusion Matrix", type="Multiclassification Evaluation")

    def evaluate(self, Y_true, Y_predicted, normalize="true", labels=[]):
        """Compute the confusion matrix
        :returns: a ndarray of shape (n_classes, n_classes)
        """
        return confusion_matrix(Y_true, Y_predicted, normalize=normalize, labels=labels)

    def plot(self, Y_true, Y_predicted, normalize="true", labels=[]):
        fig, ax = plt.subplots(figsize=(16, 12))
        heatmap(
            self.evaluate(Y_true, Y_predicted, normalize=normalize, labels=labels),
            annot=True,
            ax=ax,
        )
        ax.set_xlabel("Predicted")
        ax.set_ylabel("True")
        ax.set_title("Confusion Matrix")
        ax.xaxis.set_ticklabels(labels)
        ax.yaxis.set_ticklabels(labels[::-1])
