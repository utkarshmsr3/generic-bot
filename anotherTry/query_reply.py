import json

d = dict()
count=1
with open("infytq.txt") as f:
    while(True):
        query = f.readline()
        print(query)
        if query != '':
            reply = f.readline()
            f.readline()
            d[count] = {"query":query,"reply":reply}
            count+=1
        else:
            break
f = open("data.json","w+")
f.write(json.dumps(d))
f.close()
