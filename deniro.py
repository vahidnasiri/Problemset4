import csv
import json
data={}
with open("deniro.csv", "r" ) as infile:
    rdr = csv.reader(infile, quotechar='"', delimiter=',', skipinitialspace=True)
    thisisthefirstrow=True
    for row in rdr:
        if thisisthefirstrow:
            thisisthefirstrow=False
            continue
        if len(row)==0:
            continue
        
        data2={}
        data2["Score"]=int(row[1])
        data2["Year"]=row[0]
        
        data[row[2]]=data2

with open("deniro_json.txt","w") as outfile:
    json.dump(data, outfile, indent=4)