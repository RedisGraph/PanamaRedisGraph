#!/usr/bin/env python3

import csv
import datetime

outr=[]

with open('./data_download/panama_papers.nodes.address.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    headers = next(reader, None)
    headers= ["id", "address", "country_codes", "countries"]
    outr.append(headers)
    for row in reader:
        if row[2][-1] == '\\':
            row[2] = row[2][0:-1]
        #strip any quotes inside
        row[2] = row[2].replace('"', '')
        outr.append([row[0], row[2], row[3], row[4]])

f = open('./data_download/Address.csv', 'w')
with f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for row in outr:
        writer.writerow(row)
