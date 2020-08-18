from math import sqrt
from sklearn.base import BaseEstimator
from DTW import DTW


def KNN(test, trainSet):

    k = 5
    content = []
    ids = []
    counter=0
    results = []

    for item in trainSet:
        item = item[1]
        x = DTW(test, item)
        #print x
        content.append(x)
        ids.append(counter)
        counter += 1

    max1 = max(set(content))

    min = max1

    for j in range(0, k, 1):
        for i in range(0, len(content), 1):
            if i in results:
                continue
            if content[i] < min:
                min = content[i]
                minPos = i
        results.append(minPos)
        print minPos, " - ", content[minPos]
        min = max1

    return results

