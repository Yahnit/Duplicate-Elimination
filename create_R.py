import csv
import random
from datetime import datetime

r = 5
i = 1
file_row = [[]] 
no_of_attr = 3
g=open("R.txt","w+")
w=csv.writer(g)
w.writerow((1,)*no_of_attr)
maxsize = 1000000*2
while True:
	row = []
	for j in range(no_of_attr):
		row.append(random.choice(range(0,100)))
	if i%100==0 and i!=0:
		for k in range(r):
			w.writerow(tuple(file_row[random.randrange(len(file_row))]))
	file_row.append(row)
	i = i+1
	w.writerow(tuple(row))
	if g.tell() > maxsize:    # f.tell() gives byte offset, no need to worry about multiwide chars
            break
g.close()