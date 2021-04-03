import pandas as pd
import os

_dir = os.path.dirname(os.path.realpath(__file__))

input_file = _dir + '/input/sales_2017.xlsx'
output_file = _dir + '/output/pandas_output04.xls'

df = pd.read_excel(input_file, sheet_name='january_2017')

new_df = df[df['Customer Name'].str.startswith('J')]
print(new_df)

writer = pd.ExcelWriter(output_file)
new_df.to_excel(writer, sheet_name='jan_17_output', index=False)
writer.save()
print("pandas04.py executed")