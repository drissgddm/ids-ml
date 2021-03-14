"""
metrics.__init__.py
"""

from metrics.accuracy_score import AccuracyScore
from metrics.confusion_matrix import ConfusionMatrix
from metrics.recall import Recall


accuracy = AccuracyScore()
confusion_matrix = ConfusionMatrix()
recall = Recall()
