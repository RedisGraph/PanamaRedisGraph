#!/usr/bin/env python3

import csv
import datetime

outr = {
    'intermediary_of': [],
    'officer_of': [],
    'registered_address': [],
}

with open('./data_download/panama_papers.edges.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    headers = next(reader, None)
    for row in reader:
        outr[row[1]].append([row[0], row[2]])


for i in outr.keys():
    outcsv="./data_download/%s.csv" %(i.upper())
    f = open(outcsv, 'w')
    with f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for row in outr[i]:
            writer.writerow(row)