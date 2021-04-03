import pandas as pd

import os

_dir = os.path.dirname(os.path.realpath(__file__))

input_file = _dir + '/input/sales_2017.xlsx'
output_file = _dir + '/output/pandas_output08.xls'

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)

column_output = []
for worksheet_name, data in data_frame.items():
	column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
selected_columns = pd.concat(column_output, axis=0, ignore_index=True)
print(selected_columns)

writer = pd.ExcelWriter(output_file)
selected_columns.to_excel(writer, sheet_name='selected_columns_all_worksheets', index=False)
writer.save()
print("pandas08.py executed")