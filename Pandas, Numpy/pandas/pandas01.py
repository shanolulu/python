# pandas01.py 
import pandas as pd
import os

dir = os.path.dirname(os.path.realpath(__file__))

input_file = dir + '/supplier_data.csv'
output_file = dir + '/output/pandas_output.csv'

data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)
print('Pandas Done.')