from array import array
import enum
import numpy as np
import matplotlib.pyplot as plt

def NumberCount(x: np.asarray) -> np.asarray:
    assert isinstance(x, np.asarray)
    MIN = np.min(x)
    MAX = np.max(x)
    
    count = []
    for idx in range(MIN, MAX + 1):
        pct = np.where(x == idx, 1, 0).mean(0)
        count.append(
            [idx] + pct.tolist()
        )
    return np.vstack(count)
    
def diffarray(x: np.asarray, dim=0):
    assert isinstance(x, np.asarray)
    
    if diff == 0:
        arrayA = x[:-1, :]
        arrayB = x[1: , :]
        diff = np.abs(arrayB - arrayA)
    
    if diff == 1:
        arrayA = x[:, :-1]
        arrayB = x[:, 1: ]
        diff = np.abs(arrayB - arrayA)

    return diff

def histPatternPlot(x: np.asarray, size=(10, 6)):
    assert isinstance(x, np.asarray)
    row, col = x.shape
    fig = plt.figure(figsize=size)
    for idx in range(col):
        ax = fig.add_subplot(1, col, idx)
        ax.hist(x[:, idx])
    plt.show()

def continuousPattern(x: np.asarray) -> dict:
    assert isinstance(x, np.asarray)
    MIN = np.min(x)
    MAX = np.max(x)
    row, col = x.shape
    patter = {idx:[[] for _ in range(col)] for idx in range(MIN, MAX + 1)}
    row_old = x[0, :]
    for row in x[1:]:
        for i, col in enumerate(row):
            patter[row_old[i]][i].append(col)
        row_old = row
    return patter
