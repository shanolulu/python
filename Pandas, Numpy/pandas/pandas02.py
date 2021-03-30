# pandas02.py 
import pandas as pd
import os

dir = os.path.dirname(os.path.realpath(__file__))

input_file = dir + '/supplier_data.csv'
output_file = dir + '/output/pandas_output.csv'

df = pd.read_csv(input_file)
df['Cost'] = df['Cost'].str.strip('$').astype(float)
new_df = df.loc[(df['Supplier Name'].str.contains('Z')) | (df['Cost'] > 600.0)]
new_df.to_csv(output_file, index=False)
print(new_df)
print("Done")