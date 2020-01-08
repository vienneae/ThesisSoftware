#CONVERTS .DAT FILE TO A .CSV FILE

import numpy as np
import matplotlib.pyplot as plt
import string
import math
import csv


file = input("Enter the name of the .dat file: ")



# read flash.dat to a list of lists
datContent = [i.strip().split() for i in open(file).readlines()]

# write it as a new CSV file
with open("SDSS7.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(datContent)

    