#pip install plotly==4.5.4
#see https://plot.ly/python-api-reference/generated/plotly.graph_objects.Figure.html
#see plot.ly/
import plotly.graph_objects as  go
import plotly.offline  as  offline
import csv
import math

#Simple plotting function
def plotme(xx,yy):
    fig = go.Figure(
       data=go.Pointcloud(x=xx, y=yy),
       layout=go.Layout(
          title=go.layout.Title(text="A Scatter Plot"))
    )
    offline.plot(fig, filename='file.html',auto_open=False)


	
#load a file- this will contain comma delimited values for distance
def loadafile(flename):

    mytable =[]
    with open(flename,'r') as file:
        file_reader = csv.reader(file, delimiter=',')
        for item in file_reader:
            list_item = list(item)
            fl_item = [float(i) for i in list_item]
            mytable.append(fl_item)
    return mytable

	
#calculate Euclidean distance
def euclidean_distance(element1, element2):

    if(len(element1)!=len(element2)):
          print("values wrong length....")
          return -1

    d=0

    for x in range(0, len(element1)):
        d = d + (element1[x] - element2[x])**2
        d = math.sqrt(d)

    return d

	
#find the least distant pair of indexes using this method
def findClosest(mytable):
    dist=0.0
    val1=-1
    val2=-1

    #missing code
    for x in range(0, len(mytable)):
        for y in range(x+1, len(mytable)):
            eucl_dist = euclidean_distance(mytable[x], mytable[y])

            if (val1 == -1):
                dist = eucl_dist
                val1 = x
                val2 = y
                continue
            
            if eucl_dist<dist:
                dist = eucl_dist
                val1 = x
                val2 = y

    return val1, val2,dist

#call the methods as the script loads...

#Test
dd=euclidean_distance([4,5,6,7],[4,5,12,7])

#Load files-small file for testing, big file for final search
ed=loadafile("test_bigfile.csv")
#ed=loadafile("test_file1.csv")
#Find least distant
ee=findClosest(ed)
#print simple results
print("result",dd)
print("result2",ee[0],ee[1],ee[2])
#Plot the winning distance
plotme(ed[ee[0]],ed[ee[1]])

