import pandas as pd

input_file = 'input/sales_2017.xlsx'
output_file = 'output/pandas_output09.xls'

my_sheets = [0, 1]
threshold = 1900.0

data_frame = pd.read_excel(input_file, sheet_name=my_sheets, index_col=None)

row_list = []
for worksheet_name, data in data_frame.items():
	tempAmt = data['Sale Amount'].replace('$', '').replace(',', '').astype(float)
	row_list.append(data[ tempAmt > threshold ])
	
filtered_rows = pd.concat(row_list, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='set_of_worksheets', index=False)
writer.save()
print("pandas09.py executed")