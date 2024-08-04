import pandas as pd
import numpy as np
# Series data Structure: 1-D single datatype.
ser = pd.Series(np.random.rand(5)) #12=number of rows
print("\nrows of series data:\n",ser)

# head: by default provide 5 element from top:
print("\nHead in data:\n",ser.head(2)) #2=number of head from top required

# tail: by default provid 5 element from bottom
print("\nTail in data:\n",ser.tail(2)) #2=number of tail from bottom