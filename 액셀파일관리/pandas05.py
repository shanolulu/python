import pandas as pd
import sys

input_file = 'input/sales_2017.xlsx'
output_file = 'output/pandas_output05.xls'

data_frame = pd.read_excel(input_file, 'january_2017', index_col=None)

data_frame_column_by_index = data_frame.iloc[:, [1, 4]]

writer = pd.ExcelWriter(output_file)
data_frame_column_by_index.to_excel(writer, sheet_name='jan_17_output', index=False)
writer.save()
print("pandas05.py executed")