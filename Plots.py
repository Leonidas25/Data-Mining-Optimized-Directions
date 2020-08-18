import gmplot
import pandas as pd
from ast import literal_eval


trainSet = pd.read_csv('train_set.csv', converters={"Trajectory": literal_eval}, index_col='tripId')

trainSet = trainSet.values

route1 = trainSet[10]
route2 = trainSet[20]
route3 = trainSet[30]
route4 = trainSet[45]
route5 = trainSet[50]

longitudes = [item[1] for item in route1[1]]
latitudes = [item[2] for item in route1[1]]

print route1[0]

gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0],13)

gmap.plot(latitudes,longitudes,'cornflowerblue', edge_width=10)

gmap.draw('map1.html')


longitudes = [item[1] for item in route2[1]]
latitudes = [item[2] for item in route2[1]]

print route2[0]

gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0],13)

gmap.plot(latitudes,longitudes,'cornflowerblue', edge_width=10)

gmap.draw('map2.html')


longitudes = [item[1] for item in route3[1]]
latitudes = [item[2] for item in route3[1]]

print route3[0]

gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0],13)

gmap.plot(latitudes,longitudes,'cornflowerblue', edge_width=10)

gmap.draw('map3.html')


longitudes = [item[1] for item in route4[1]]
latitudes = [item[2] for item in route4[1]]

print route4[0]

gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0],13)

gmap.plot(latitudes,longitudes,'cornflowerblue', edge_width=10)

gmap.draw('map4.html')


longitudes = [item[1] for item in route5[1]]
latitudes = [item[2] for item in route5[1]]

print route5[0]

gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0],13)

gmap.plot(latitudes,longitudes,'cornflowerblue', edge_width=10)

gmap.draw('map5.html')