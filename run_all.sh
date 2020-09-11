#!/bin/bash

rm -f relationships.png
dot -T png relationships.dot > relationships.png

python3 data_cleaners/clean_entities.py
python3 data_cleaners/clean_officers.py
python3 data_cleaners/clean_addresses.py
python3 data_cleaners/clean_intermediary.py
