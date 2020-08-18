import numpy as np
import haversine


def DTW(x, y):

    distanceMatrix = np.zeros((len(x), len(y)))

    for i in range(0, len(x), 1):
        for j in range(0, len(y), 1):

            dx = [x[i][1], x[i][2]]
            dy = [y[j][1], y[j][2]]

            distance = haversine.haversine(dx, dy)

            if i > 0 and j > 0:
                distanceMatrix[i][j] = distance + min(distanceMatrix[i-1][j], distanceMatrix[i-1][j-1], distanceMatrix[i][j-1])

            elif i == 0 and j > 0:
                distanceMatrix[i][j] = distance + distanceMatrix[i][j-1]

            elif i > 0 and j == 0:
                distanceMatrix[i][j] = distance + distanceMatrix[i-1][j]

            else:
                distanceMatrix[i][j] = distance

    maximum = distanceMatrix[len(x)-1][len(y)-1]
    i=len(x)-1
    j=len(y)-1

    while i > 0 or j > 0:

        if i > 0 and j > 0 and distanceMatrix[i-1][j-1] == min(distanceMatrix[i-1][j], distanceMatrix[i-1][j-1], distanceMatrix[i][j-1]):
            maximum += distanceMatrix[i-1][j-1]
            i -= 1
            j -= 1

        elif i > 0 and j > 0 and distanceMatrix[i][j-1] == min(distanceMatrix[i-1][j], distanceMatrix[i-1][j-1], distanceMatrix[i][j-1]):
            maximum += distanceMatrix[i][j-1]
            j -= 1

        elif i > 0 and j > 0 and distanceMatrix[i-1][j] == min(distanceMatrix[i-1][j], distanceMatrix[i-1][j-1], distanceMatrix[i][j-1]):
            maximum += distanceMatrix[i-1][j]
            i -= 1

        elif i == 0 and j > 0:
            maximum += distanceMatrix[i][j-1]
            j -= 1

        elif i > 0 and j == 0:
            maximum += distanceMatrix[i-1][j]
            i -= 1

        else:
            print "Should never be printed!"

    return maximum


