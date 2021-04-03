import pandas as pd
import glob
import os

_dir = os.path.dirname(os.path.realpath(__file__))

input_path = _dir + '/input'
output_file = _dir + '/output/pandas_output10.xls'

all_workbooks = glob.glob(os.path.join(input_path,'*.xls*'))
data_frames = []
for workbook in all_workbooks:
	all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
	for worksheet_name, data in all_worksheets.items():
		data_frames.append(data)

all_data_concatenated = pd.concat(data_frames, axis=1, ignore_index=True)
print(all_data_concatenated)

writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index=False)
writer.save()
print("pandas10.py executed")