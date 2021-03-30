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
    total_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) for value in df.loc[:, 'Sale Amount']]).sum()
    # average_sales 
    avg_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) for value in df.loc[:, 'Sale Amount']]).mean()

    data = {'file_name': os.path.basename(input_file), 'total_sales': total_sales, 'avg_sales': avg_sales}

    all_data_frames.append(pd.DataFrame(data, columns=['file_name', 'total_sales', 'avg_sales']))

all_data_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
print(all_data_concat)
all_data_concat.to_csv(output_file, index=False)
print('Done')
