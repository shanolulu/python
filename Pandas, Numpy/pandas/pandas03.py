# pandas02.py 
import pandas as pd
import os

dir = os.path.dirname(os.path.realpath(__file__))

input_file = dir + '/supplier_data.csv'
output_file = dir + '/output/pandas_output.csv'

df = pd.read_csv(input_file)
filter_date = ['1/20/14','1/30/14']
notin_filter_date = ['2002-03-14']

filtered_df = df['Purchase Date'].isin(filter_date) # not in
print(filtered_df)
new_df = df.loc[filtered_df]
print(new_df)
new_df.to_csv(output_file, index=False)