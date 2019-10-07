import csv
import numpy

with open("144.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        print('line[{}] = {}'.format(i, line))

