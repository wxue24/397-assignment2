import numpy

# Index of each inner array represents starting location
# Each tuple represents end location and probability

STM: list[list[tuple[int, float]]] = [
    [(1, 0.3), (2, 0.1), (3, 0.6)],
    [(2, 0.5), (3, 0.5)],
    [(3, 0.2), (4, 0.2), (5, 0.3), (6, 0.3)],
    [(7, 1)],
    [(8, 1)],
    [(9, 1)],
    [(9, 1)],
    [(6, 1)],
    [(5, 0.5), (9, 0.5)],
    [(9, 1)],
]

# Below are used for value function calculation
REWARDS = numpy.array([-1, -1, -1, 2, -1, -1, 2, -1, 2, 15])
PROBABILITIES = numpy.matrix(
    [
        [0, 0.3, 0.1, 0.6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0.2, 0.2, 0.3, 0.3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0.5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]
)
IDENTITY = numpy.identity(10)
