#!/usr/bin/env python3

import csv
import datetime

outr=[]

with open('./data_download/panama_papers.nodes.intermediary.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    headers = next(reader, None)
    headers[0] = "id"
    outr.append(headers[0:4])
    for row in reader:
        if row[1][-1] == '\\':
            row[1] = row[1][0:-1]
        row[1]=row[1].upper()
        outr.append(row[0:4])

f = open('./data_download/Intermediary.csv', 'w')
with f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for row in outr:
        writer.writerow(row)
