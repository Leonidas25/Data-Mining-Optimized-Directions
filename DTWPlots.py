import gmplot
import pandas as pd
from ast import literal_eval


trainSet = pd.read_csv('train_set.csv', converters={"Trajectory": literal_eval}, index_col='tripId')
testSet = pd.read_csv('test_set_a1_t.csv', converters={"Trajectory": literal_eval},sep="\t")

testSet = testSet[4:5]
testSet = testSet.values
testSet = testSet[0][0]

print testSet

longitudes = [item[1] for item in testSet]
latitudes = [item[2] for item in testSet]

gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0],13)

gmap.plot(latitudes,longitudes,'cornflowerblue', edge_width=10)

gmap.draw('mapTest.html')


trainSet = trainSet.values

route1 = trainSet[1425]
route2 = trainSet[5016]
route3 = trainSet[1423]
route4 = trainSet[312]
route5 = trainSet[1429]

longitudes = [item[1] for item in route1[1]]
latitudes = [item[2] for item in route1[1]]

print route1[0]

gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0],13)

gmap.plot(latitudes,longitudes,'cornflowerblue', edge_width=10)

gmap.draw('map1425.html')


longitudes = [item[1] for item in route2[1]]
latitudes = [item[2] for item in route2[1]]

print route2[0]

gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0],13)

gmap.plot(latitudes,longitudes,'cornflowerblue', edge_width=10)

gmap.draw('map5016.html')


longitudes = [item[1] for item in route3[1]]
latitudes = [item[2] for item in route3[1]]

print route3[0]

gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0],13)

gmap.plot(latitudes,longitudes,'cornflowerblue', edge_width=10)

gmap.draw('map1423.html')


longitudes = [item[1] for item in route4[1]]
latitudes = [item[2] for item in route4[1]]

print route4[0]

gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0],13)

gmap.plot(latitudes,longitudes,'cornflowerblue', edge_width=10)

gmap.draw('map312.html')


longitudes = [item[1] for item in route5[1]]
latitudes = [item[2] for item in route5[1]]

print route5[0]

gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0],13)

gmap.plot(latitudes,longitudes,'cornflowerblue', edge_width=10)

gmap.draw('map1429.html')