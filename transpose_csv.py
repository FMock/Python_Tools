#!/usr/bin/env python
import sys
import csv

# transpose_csv.py by Frank Mock 12/26/12017
# This script will transpose the contents of a CSV file
# Despite the name of the script, you must specify the delimiter
# Usage: ./transpose_csv.py fileName "delimiter"

# Get line count of a file
def file_len(fname):
    with open(fname) as f:
        i = 0
        for i, l in enumerate(f):
            pass
    return i + 1

# Get the number of columns of CSV file
def col_count(fname, delim):
    with open(fname) as f:
        l = f.readline()
        l2 = l.split(delim)
        return len(l2)
    
fileName = ""
delimiter = ""

# Check for the correct number of arguments
c = sys.argv
if len(c) < 3:
    print("Not enough arguments. Usage: ./transpose_csv.py fileName delimiter")

else:
    fileName = sys.argv[1]
    delimiter = sys.argv[2]
    cols = col_count(fileName, delimiter)
    rows = file_len(fileName)

    # Create a list of lists named transposed
    transposed = list()
    for i in range(cols):
        transposed.append(list())

    # Transpose the data and save in transposed
    with open(fileName, "r") as f:
        for r in range(rows):
            text = f.readline()
            L = text.split(delimiter)
            for c in range(len(L)):
                transposed[c].append(L[c])

    for n in range(len(transposed)):
        print(transposed[n])
