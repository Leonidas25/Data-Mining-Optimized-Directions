from math import sqrt
from sklearn.base import BaseEstimator
from DTW import DTW


class KNN(BaseEstimator):

    k = 5
    categories = []
    content = []

    def findDistance(self, x, y):

        return DTW(x, y)

    def fit(self, x, y):

        self.categories = y
        self.content = x


    def predict(self, x):

        result = []

        l = len(self.content)

        for i in range(0, len(x), 1):

            values = []
            positions = []

            for p in range(0, self.k, 1):
                for j in range(0, l, 1):
                    if j in positions:
                        continue
                    d = self.findDistance(self.content[j], x[i])
                    if j == 0:
                        minimum = d
                        minpos = 0
                    if d < minimum:
                        minimum = d
                        minpos = j
                positions.append(minpos)

            for p in range(0, self.k, 1):
                values.append(self.categories[positions[p]])

            print values

            minpos = max(set(values), key=values.count)

            result.append(minpos)

        return result
