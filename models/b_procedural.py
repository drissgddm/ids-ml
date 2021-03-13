""" models.b_procedural.py
Model class: ProceduralBaseline1, ProceduralBaseline2, ProceduralBaseline3
"""
from datamodels.metric import Model

from random import randint


class ProceduralBaseline1(Model):
    def __init__(self):
        super().__init__(
            name="Procedural Baseline based on IP addresses and protocols",
            type="Procedural",
        )

    def apply_preprocessing(self):
        pass

    def train(self):
        pass

    def predict(self, X):
        # 0 if PROTOCOL NOT IN ('TCP', 'UDP') AND SRC_IP != '192.168' else random
        return [
            0
            if row["PROTOCOL"] not in range(2)
            or row["SRC_IP_ADDR"] not in [21284, 21265]
            else randint(1, 4)
            for _, row in X.iterrows()
        ]


class ProceduralBaseline2(Model):
    def __init__(self):
        super().__init__(
            name="Procedural Baseline based on IP addresses and TOS",
            type="Procedural"
        )

    def apply_preprocessing(self):
        pass

    def train(self):
        pass

    def predict(self, X):
        # 0 if TOS NOT IN ('32', '16') AND DST_IP != 192.168.100.6 else random
        return [
            0 if row["TOS"] in (2, 1) or row["DST_IP_ADDR"] != 21265 else randint(1, 4)
            for _, row in X.iterrows()
        ]


class ProceduralBaseline3(Model):
    def __init__(self):
        super().__init__(
            name="Random Baseline", type="Random"
        )

    def apply_preprocessing(self):
        pass

    def train(self):
        pass

    def predict(self, X):
        return [0 for _ in range(len(X))]
