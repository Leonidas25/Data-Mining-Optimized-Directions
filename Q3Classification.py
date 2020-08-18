import pandas as pd
from ast import literal_eval
from KNNDTW import KNN

nList = []
jList = []
neighbors = []

testSet = pd.read_csv('test_set_a2_t.csv', converters={"Trajectory": literal_eval},sep="\t")
trainSet = pd.read_csv('train_set.csv', converters={"Trajectory": literal_eval},index_col='tripId')


trainSetTemp = trainSet.values

for j in range(0, 5):
    testSetTemp = testSet[j:j+1]

    testSetTemp = testSetTemp.values

    testSetTemp = testSetTemp[0][0]

    neighbors = KNN(testSetTemp, trainSetTemp)

    print "Nearest Neighbors:"
    print "ROUND %d" % j

    jList = [trainSetTemp[item][0] for item in neighbors]

    #print neighbors
    #print jList
    #print "Max: ", max(set(jList), key=jList.count)

    nList.append(max(set(jList), key=jList.count))

    #for i in range(0, len(neighbors), 1):

        #nList.append(neighbors[i])
        #jList.append(trainSetTemp[neighbors[i]][0])

d = {'Test_Trip_ID': [i for i in range(1, len(testSet.values)+1, 1)]}
d['Predicted_JourneyPatternID'] = nList

#print d

df = pd.DataFrame(data=d)
dff = df[['Test_Trip_ID', 'Predicted_JourneyPatternID']]

dff.to_csv(path_or_buf="testSet_JourneyPatternIDs.csv", sep='\t', index=False)