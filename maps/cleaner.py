import pandas as pd
import numpy as np
from matplotlib import pyplot as pt


dataset = pd.read_csv('farmer.csv')

pd.set_option('display.max_rows',2000)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

#toDrop = [ 'UNIX TIME','TIME', 'DIST', 'HR', 'CAD', 'TEMP', 'POWER']

#dataset.drop(columns=toDrop, inplace=True, axis=1)

#save csv
#df= pd.DataFrame(dataset)
#df.to_csv('cleaned.csv')
print(dataset)

