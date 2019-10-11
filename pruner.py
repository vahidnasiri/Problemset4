import json

data = {}
with open("baby_names.txt","r") as infile:
    data = json.load(infile)
#print(data)
#name = {}
#for key, value in data.items() :
    #name= value

#print(data["top"])
subs = 'v' 
res = [i for i in data["top"].keys() if subs in i]
name ={k:v for k,v in data["top"].items() if k!= res[0] and k!=res[1] and k!=res[2]}

name = { k : v for k,v in data["top"].items() if k!='Gary' and k!='Aaron' and k!= 'Winston' and k!='Avery' and k!= 'Luke'}

name = { k : v for k,v in data["top"].items() if v!='28'}

name['Ron'] = '5'

data["top"]=name

with open("better_name.txt","w") as outfile:
    json.dump(data, outfile, indent=4)