"""
models.__init__.py
"""

from models.b_random import RandomBaseline
from models.b_procedural import (
    ProceduralBaseline1,
    ProceduralBaseline2,
    ProceduralBaseline3,
)


random = RandomBaseline()
procedural1 = ProceduralBaseline1()
procedural2 = ProceduralBaseline2()
procedural3 = ProceduralBaseline3()