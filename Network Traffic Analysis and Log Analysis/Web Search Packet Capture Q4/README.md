# Web Search Packet Capture Q4(20)

## Description:
	How many unique queries did the user search for?

## Solution

The Filtered pcap file was then exported as a CSV file and used to record all the unique queries using the a short python program.

```python
import csv

list=[]
with open('Q4.csv','r') as mycsv:
	csv_reader=csv.reader(mycsv,delimiter=',')
	for row in csv_reader:
		for i in row:
			if '?q' in i and i[15:25] not in list:
				list.append(i[15:25])
print(len(list))
```				


