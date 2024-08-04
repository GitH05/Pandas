import pandas as pd
import numpy as np
# Series data Structure: 1-D single datatype.
ser = pd.Series(np.random.rand(5)) #12=number of rows
print("\nrows of series data:\n",ser)
print(type(ser))    #type
# index
print(ser.index)
# series data type 
print(ser.dtype)