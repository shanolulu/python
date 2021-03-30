# pandas04.py 
import pandas as pd
import os

dir = os.path.dirname(os.path.realpath(__file__))

input_file = dir + '/supplier_data.csv'
output_file = dir + '/output/pandas_output.csv'

df = pd.read_csv(input_file)
new_df = df.iloc[:, [0, 3]]
print(new_df)
new_df.to_csv(output_file, index=False)