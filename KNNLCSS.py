from math import sqrt
from sklearn.base import BaseEstimator
from DTW import DTW
from LCSS import LCSS, LCSS_Trajectory

def KNN(test, trainSet):

    k = 5
    content = []
    ids = []
    counter=0
    results = []

    for item in trainSet:
        item = item[1]
        x = LCSS(test, item)
        #print x
        content.append(x)
        ids.append(counter)
        counter += 1

    max1 = 0
    maxPos = 0

    for j in range(0, k, 1):
        for i in range(0, len(content), 1):
            if i in results:
                continue
            if content[i] > max1:
                max1 = content[i]
                maxPos = i
        results.append(maxPos)

        print maxPos, " - ", content[maxPos]
        print LCSS_Trajectory(test, trainSet[maxPos][1])
        max1 = 0

    return results

