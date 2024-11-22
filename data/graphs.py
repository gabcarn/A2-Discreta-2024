G_Crow = {
    0: [1, 2, 3, 4, 5], # 0 | 0
    1: [0, 2, 5],       # 1 | 1
    2: [0, 1, 3],       # 2 | 2
    3: [0, 2, 4],       # 1 | 3
    4: [0, 3, 5],       # 3 | 4
    5: [0, 1, 4]        # 4 | 5
}                       # X | G


G_10_9_4 = {
    0: [1, 2, 3],      # 0 | 0
    1: [0, 2, 3],      # 1 | 1
    2: [0, 1, 3],      # 2 | 2
    3: [0, 1, 2, 4],   # 3 | 3
    4: [3, 5],         # 0 | 4
    5: [4, 6],         # 1 | 5
    6: [5, 7],         # 0 | 6
    7: [6, 8],         # 1 | 7
    8: [7, 9],         # 0 | 8
    9: [8]             # 1 | 9
}                      # X | G

G_10_9_6 = {
    0: [1, 2, 3, 4, 5],  # 0 | 0
    1: [0, 2, 3, 4, 5],  # 1 | 1
    2: [0, 1, 3, 4, 5],  # 2 | 2
    3: [0, 1, 2, 4, 5],  # 3 | 3
    4: [0, 1, 2, 3, 5],  # 4 | 4
    5: [0, 1, 2, 3, 4],  # 5 | 5
    6: [7],              # 0 | 0
    7: [6, 8],           # 1 | 1
    8: [7, 9],           # 0 | 2
    9: [8]               # 1 | 3
}                        # X | G

K2 = {
    0: [1],
    1: [0]
}

K3 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

K4 = {
    0: [1, 2, 3],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [0, 1, 2]
}

K4_uncompleted = {
    0: [1, 2, 3],
    1: [0, 2, 3],
    2: [0, 1],
    3: [0, 1]
}

K5_uncompleted = {
    0: [1, 2, 3, 4],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [0, 1, 2],
    4: [0, 1, 2]
}