import pandas as pd
import numpy as np
from ast import literal_eval
import haversine
from DTW import DTW
from KNNLCSS import KNN
from LCSS import LCSS_Trajectory
import time

list1=[]
list2=[]

start_time = time.time()

testSet = pd.read_csv('test_set_a2_t.csv', converters={"Trajectory": literal_eval},sep="\t")
trainSet = pd.read_csv('train_set.csv', converters={"Trajectory": literal_eval},index_col='tripId')

testSet = testSet[4:5]

testSet = testSet.values
trainSet = trainSet.values

testSet = testSet[0][0]

#print testSet

neighbors = KNN(testSet, trainSet)

print "Nearest Neighbors:"
for i in range(0, len(neighbors), 1):
    print trainSet[neighbors[i]][0]

print time.time() - start_time