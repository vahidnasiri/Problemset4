import sys

if len(sys.argv) <= 1:
    print("Usage: python " + sys.argv[0] + " <song file name>")
    sys.exit()

d={}

for songname in sys.argv[1:]:
    #print (songname)
    with open(songname) as infile:
    
        text=infile.readlines()
        #print(line[0])
        firstline=True
        title = ""
        for line in text: 
            if firstline:
                firstline=False
                title = line
                print(title)
                continue
             
         
            line = line.strip() 
             
            line = line.lower() 
             
            words = line.split(" ") 

            for word in words: 
                 
                if word in d: 
                    
                    d[word]["Count"] = d[word]["Count"] + 1
                    if title not in d[word]['Songs']:
                        d[word]["Songs"].append(title)
                else: 
                
                    d[word] = {"Count":1, "Songs":[title]}
     
            print(d)