#!/usr/bin/env python3

import csv
import datetime

outr=[]

with open('./data_download/panama_papers.nodes.entity.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    headers = next(reader, None)
    headers[0] = "id"
    outr.append(headers[0:10])
    for row in reader:
        if row[6] != "":
            row[6]=datetime.datetime.strptime(row[6], '%d-%b-%Y').strftime('%s')
        else:
            row[6]=0
        if row[7] != "":
            row[7]=datetime.datetime.strptime(row[7], '%d-%b-%Y').strftime('%s')
        else:
            row[7]=9999999999
        if row[8] != "":
            row[8]=datetime.datetime.strptime(row[8], '%d-%b-%Y').strftime('%s')
        else:
            row[8]=9999999999
        if row[9] != "":
            row[9]=datetime.datetime.strptime(row[9], '%d-%b-%Y').strftime('%s')
        else:
            row[9]=9999999999
        outr.append(row[0:10])

f = open('./data_download/Entity.csv', 'w')
with f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for row in outr:
        writer.writerow(row)
