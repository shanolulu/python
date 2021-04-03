import pandas as pd

input_file = 'input/sales_2017.xlsx'
output_file = 'output/pandas_output06.xls'

df = pd.read_excel(input_file, sheet_name='january_2017')

# new_df = df[df['Customer Name'].str.startswith('J')]
# new_df = df.iloc[:,[1,4]]
new_df = df.loc[:, ['Customer ID', 'Customer Name', 'Purchase Date']]

print(new_df)

writer = pd.ExcelWriter(output_file)
new_df.to_excel(writer, sheet_name='jan_17_output', index=False)
writer.save()
print("pandas06.py executed")