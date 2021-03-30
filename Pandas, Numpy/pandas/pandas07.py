# pandas04.py 
import pandas as pd
import os

dir = os.path.dirname(os.path.realpath(__file__))

input_file = dir + '/supplier_data.csv'
output_file = dir + '/output/pandas_output.csv'

df = pd.read_csv(input_file, header=None)
df = df.drop([0,1,2,11,12])
print(df)
new_df = df.reindex()
print("# after reindex")
print(new_df.reset_index())