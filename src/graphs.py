

hossein = {
    "V": {
        1: (1, (-2, 1)),
        2: (1, (-2, -1)),
        3: (1, (-1, 0)),
        4: (3, (1, 0)),
        5: (3, (2, 1)),
        6: (3, (2, -1))
    },
    "E": {
        3: [1, 2, 4],
        4: [5, 6]
    }
}

cross = {
    "V": {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5
    },
    "E": {
        1: [2, 3, 4, 5]
    }
}

triangle = {
    "V": {
        1: (2, (0, 1)),
        2: (0, (-1, -1)),
        3: (1000000, (1, -1)),
    },
    "E": {
        1: [2],
        2: [3],
        3: [1],
    }
}

square = {
    "V": {
        1: (-10000, (-1, 1)),
        2: (1, (1,  1)),
        3: (1, (-1, -1)),
        4: (100000, (1,  -1)),
    },
    "E": {
        1: [2, 3, 4],
        2: [3, 4],
        3: [4],
        4: [1]
    }
}

pentagon = {
    "V": {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5
    },
    "E": {
        1: [2],
        2: [3],
        3: [4],
        4: [5],
        5: [1]
    }
}

pentagram = {
    "V": {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5
    },
    "E": {
        1: [2, 3, 4],
        2: [3, 4, 5],
        3: [4, 5],
        4: [5],
        5: [1]
    }
}

hexagon = {
    "V": {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6
    },
    "E": {
        1: [2],
        2: [3],
        3: [4],
        4: [5],
        5: [6],
        6: [1]
    }
}

line = {
    "V": {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5
    },
    "E": {
        1: [2],
        2: [3],
        3: [4],
        4: [5],
        4: [5]
    }
}
