""" embeddings.b_node2vec.py
Model class: Node2VecBaseline
"""
from datamodels.embedding import Embedding

from node2vec import Node2Vec


class Node2VecBaseline(Embedding):
    """Node2VecBaseline Embedding class"""

    def __init__(self, node2vec=None):
        super().__init__(name="Node2Vec baseline", type="Node2Vec")
        self.node2vec = node2vec

    @classmethod
    def from_networkx_graph(
        cls, networkx_graph, dimensions=1000, walk_length=10, num_walks=100, p=1, q=1
    ):
        return cls(
            Node2Vec(
                networkx_graph,
                dimensions=dimensions,
                walk_length=walk_length,
                num_walks=num_walks,
                p=p,
                q=q,
            )
        )

    def fit(self, window=10, min_count=1):
        self.model = self.node2vec.fit(window=window, min_count=min_count)
        self.node_embeddings = self.model.wv.vectors
        self.node_embeddings_id = self.model.wv.index2word

    def optimize_hyperparameters(self):
        pass
