'''PROJECT 2 286
	GROUP NUMBER: 8'''
	
import csv
with open("Project2Results.csv","r") as f:
    r=csv.reader(f)
    l=[]
    l1=[]
    l2=[]
    for row in r:
        print(row)
        l.append(row[3])
        l1.append(row[1])
        l2.append(row[2])
    l3=[]
    le=len(l2)
    for item in range(1,le):
        l3.append(l2[item])
        print(l3)
    print("TOTAL PACKETS RECEIVED:", sum(list(map(int,l3))))
        
    #print("Receive rate:",l1)
    #print("Packets received:",l2)
    #print("Number of Sinks:",l)
