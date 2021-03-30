# pandas08.py 
import pandas as pd
import os, glob, sys

dir = os.path.dirname(os.path.realpath(__file__))

input_path = dir + '/'
output_file = dir + '/output/pandas_output.csv'

all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []

for input_file in all_files:
    df = pd.read_csv(input_file, index_col=None)
    all_data_frames.append(df)

all_data_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
print(all_data_concat)
all_data_concat.to_csv(output_file, index=False)
print('Done')
