import pandas as pd

import os

_dir = os.path.dirname(os.path.realpath(__file__))

input_file = _dir + '/input/sales_2017.xlsx'
output_file = _dir + '/output/pandas_output07.xls'

df = pd.read_excel(input_file, sheet_name=None)

row_output = []
for worksheet_name, data_frame in df.items():
    row_output.append(data_frame[data_frame['Sale Amount'].replace('$', '').replace(',','').astype(float) > 2000.0])

new_df = pd.concat(row_output, axis=0, ignore_index=True)
print(new_df)

writer = pd.ExcelWriter(output_file)
new_df.to_excel(writer, sheet_name='sale_amount', index=False)
writer.save()
print("pandas07.py executed")