import csv

list=[]
with open('Q4.csv','r') as mycsv:
	csv_reader=csv.reader(mycsv,delimiter=',')
	for row in csv_reader:
		for i in row:
			if '?q' in i and i[15:25] not in list:
				list.append(i[15:25])
print(len(list))
				


