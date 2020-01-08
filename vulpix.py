# Attempt to feed values from the .csv files into the calculator
import numpy as np
import matplotlib.pyplot as plt
import string
import math
import csv
import pandas as pd
import os
import subprocess


data = pd.read_csv("groupGalaxies.csv")

z = data.redshift.tolist()

plateScale = list()

n=0
for j in z:
    n=n+1
    print(("%d / %d" % (n, len(z))))
    x = os.popen('python cosmocalc_prime.py %s' % j).read()
    for i in range(0, len(x)-1):
        if x[i] == 'P':
            if x[i+1] == 'S':
                if x[i+2] == '_':
                    if x[i+3] == 'k':
                        x = x[i+9:i+20]
                        break;

    plateScale.append(x)
   


data['plateScale'] = plateScale  

plateScale = data.plateScale.tolist()
rD = data.disk_rd.tolist()
rD_kPc = list()
#sfr = data.sfr.tolist()
#sM = data.logTotalStellarMass.tolist()
#sfr_sM = list()

for i in range(0, len(rD)):
    rD_kPc.append(float(plateScale[i])*float(rD[i]))
#for i in range(0, len(sM)):
#    sfr_sM.append(float(sfr[i])-float(sM[i]))
    
    
data['diskHalfLightRadius_kPc'] = rD_kPc
#data['log(sfr/sm)'] = sfr_sM


data.to_csv("groupGalaxiesTEST.csv", sep=',', index=False)
print("Complete.")

