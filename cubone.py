import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def myFunction(file):

    data = pd.read_csv(file)

    groupID = data.parentGroupID.tolist()
    ra = data.ra_ofGalaxy.tolist()
    dec = data.dec_ofGalaxy.tolist()
    redshift = data.z_ofGalaxy.tolist()
    ls = list()

    

    n = 0
    for i in groupID:
        if (groupID.count(i) >= 3 and ls.count(i) == 0):
            ls.append(i)

    

    print(len(ls) , "groups with >= 3 members")

    groupIDPrime = list()
    raPrime = list()
    decPrime = list()
    redshiftPrime = list()




    n=0
    for k in groupID:
        if (k in ls):
            print(k)
            groupIDPrime.append(groupID[n])
            raPrime.append(ra[n])
            decPrime.append(dec[n])
            redshiftPrime.append(redshift[n])
            n = n+1

    

    print(n , "galaxies")

    df = pd.DataFrame({'GroupID': groupIDPrime, 'ra': raPrime, 'dec': decPrime, 'redshift': redshiftPrime})

    df.to_csv("groups.csv")




myFunction("imodelC_1_SDSS7.csv")


