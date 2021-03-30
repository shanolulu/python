import pandas as pd
import numpy as np
# 1,2,3
# 4,5,6

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))
print("DataFrame #1")
print(df.shape)
print(len(df.index))
print(list(df.columns))
print(df)
# list[], tuple(), dictionary{key,value}
df = pd.DataFrame({"A": [1,4,7], "B": [2,5,8], "C":[3,6,9]})
print("DataFrame #2")
print(df.loc[0])
print(df.loc[:, 'A'])
print(df.loc[1:, 'B'])
print(df)
