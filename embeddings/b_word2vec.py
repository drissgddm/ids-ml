""" embeddings.b_word2vec.py
Model class: Word2VecBaseline
"""
from datamodels.embedding import Embedding

from stellargraph.data import BiasedRandomWalk
from stellargraph import StellarGraph
from gensim.models import Word2Vec


class Word2VecBaseline(Embedding):
    """Word2VecBaseline Embedding class"""

    def __init__(self, word2vec=None):
        super().__init__(name="Word2Vec baseline", type="Word2Vec")
        self.word2vec = word2vec

    @classmethod
    def from_networkx_graph(
        cls, networkx_graph, size=128, window=5, min_count=0, sg=1, workers=2, iter=1
    ):
        rw = BiasedRandomWalk(StellarGraph(networkx_graph))
        walks = (
            [
                list(map(str, walk))
                for walk in rw.run(
                    nodes=list(networkx_graph.nodes()),  # root nodes
                    length=100,  # maximum length of a random walk
                    n=10,  # number of random walks per root node
                    p=0.5,  # Defines (unormalised) probability, 1/p, of returning to source node
                    q=2.0,  # Defines (unormalised) probability, 1/q, for moving away from source node
                )
            ],
        )
        return cls(
            word2vec=Word2Vec(
                walks, size=128, window=5, min_count=0, sg=1, workers=2, iter=1,
            )
        )

    def fit(self, window=10, min_count=1):
        self.model = self.node2vec.fit(window=window, min_count=min_count)
        self.node_embeddings = self.model.wv.vectors
        self.node_embeddings_id = self.model.wv.index2word

    def optimize_hyperparameters(self):
        pass
