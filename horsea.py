

import pandas, sys
import pandas as pd

a = pd.read_csv("void3Galaxies.csv")
b = pd.read_csv("void4Galaxies.csv")

merged = a.merge(b, on='1_1')

merged.to_csv('voidGalaxies.csv', index=False)
