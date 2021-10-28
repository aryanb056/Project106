import csv
import numpy as np

def getDataSource(path):
    marks=[]
    days=[]
    with open(path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["marks"]))
            days.append(float(row["days"]))

    return{"x":marks,"y":days}

    
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between days and marks",correlation[0,1])

def setup():
    path="marks.csv"
    datasource=getDataSource(path)
    findcorrelation(datasource)

setup()