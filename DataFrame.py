import pandas as pd
import numpy as np
# DataFrame: 2-D array:
# creation:
df = pd.DataFrame(np.random.rand(6,6),index=np.arange(6))   #6=row,6=column
print(df)
# type
print(type(df))
# column 
print(df.columns)
# index
print(df.index)
# to convert into array:
print("\nInto Array:\n",df.to_numpy())
# save file into file format
df.to_csv('RandomData.csv')
# read file
newdf = pd.read_csv('student_clustering.csv')
print("\nStudent Clustering\n",newdf)