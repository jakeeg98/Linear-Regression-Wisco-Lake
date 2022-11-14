import csv
import sys
import math
import numpy as np
from pandas import *
import matplotlib.pyplot as plt


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filepath = sys.argv[1]
    # filepath = "toy.csv"
    print(filepath)
    filename = open(filepath, 'r')
    file = csv.DictReader(filepath)
    # print(file)
    yearVec = []
    for col in file:
        yearVec.append([1, int(col['year'])])

    print(yearVec)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
