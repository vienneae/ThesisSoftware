import numpy as np
import matplotlib.pyplot as plt
import string
import math
import csv
import pandas


# SELECTING OUT GALAXIES THAT HAVE A B/T RATIO LESS THAN 'x':
x = 0.3

# FILE: 'void3Galaxies.csv':
colnames = ['raV3', 'decV3', 'totAppMagV3', 'btV3', 'totHalfLightRadV3', 'semiMaj/MinRatio']
data = pandas.read_csv("void3Galaxies.csv", usecols=[18,19,31], names = colnames)
raV3 = data.raV3.tolist()
decV3 = data.decV3.tolist()
btV3 = data.btV3.tolist()
i = 0
while i < len(btV3):
    if btV3[i] == -999.0 or btV3[i] > x:
        print( btV3[i])
        btV3.pop(i)
        raV3.pop(i)
        decV3.pop(i)
        i = i -1
    i = i + 1

# FILE: 'void4Galaxies.csv':
colnames = ['raV4', 'decV4', 'btV4']
data = pandas.read_csv("void4Galaxies.csv", usecols=[18,19,31], names = colnames)
raV4 = data.raV4.tolist()
decV4 = data.decV4.tolist()
btV4 = data.btV4.tolist()
i = 0
while i < len(btV4):
    if btV4[i] == -999.0 or btV4[i] > x:
        print( btV4[i])
        btV4.pop(i)
        raV4.pop(i)
        decV4.pop(i)
        i = i -1
    i = i + 1

# FILE: 'filamentGalaxies.csv':
colnames = ['raF', 'decF', 'btF']
data = pandas.read_csv("filamentGalaxies.csv", usecols=[18,19,31], names = colnames)
raF = data.raF.tolist()
decF = data.decF.tolist()
btF = data.btF.tolist()
i = 0
while i < len(btF):
    if btF[i] == -999.0 or btF[i] > x:
        print( btF[i])
        btF.pop(i)
        raF.pop(i)
        decF.pop(i)
        i = i -1
    i = i + 1


# File Creation

dfV3 = pandas.DataFrame(data={"col1": raV3, "col2": decV3, "col3": btV3})
dfV3.to_csv("<0.3void3Galaxies.csv", sep=',',index=False)

dfV4 = pandas.DataFrame(data={"col1": raV4, "col2": decV4, "col3": btV4})
dfV4.to_csv("<0.3void4Galaxies.csv", sep=',',index=False)

dfF = pandas.DataFrame(data={"col1": raF, "col2": decF, "col3": btF})
dfF.to_csv("<0.3filamentGalaxies.csv", sep=',',index=False)