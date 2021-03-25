""" dim_reducer.b_tsne.py
Model class: tSNEBaseline
"""
from datamodels.dim_reducer import DimensionsReducer

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


class tSNEBaseline(DimensionsReducer):
    """tSNEBaseline dimensions reducer class"""

    def __init__(self, n_components=2, perplexity=30, n_iter=1000, verbose=1):
        super().__init__(name=" t-SNE baseline", type="t-SNE")
        self.tsne = TSNE(
            n_components=n_components,
            perplexity=perplexity,
            n_iter=n_iter,
            verbose=verbose,
        )

    def fit(self, vectors):
        self.reduced_vectors = self.tsne.fit_transform(vectors)
        return self.reduced_vectors

    def plot(self, colors=[]):
        plt.figure(figsize=(15, 10))
        plt.scatter(
            self.reduced_vectors[:, 0],
            self.reduced_vectors[:, 1],
            c=colors,
            cmap="jet",
            alpha=0.5,
        )
