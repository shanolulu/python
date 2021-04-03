from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

input_file = 'input/sales_2017.xlsx'
output_file = 'output/output02.xls' # or use openpyxl for xlsx

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2017_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2017')
    
    for row_index in range(worksheet.nrows):
        for col_index in range(worksheet.ncols):
            output_worksheet.write(row_index, col_index, \
                                        worksheet.cell_value(row_index, col_index))

output_workbook.save(output_file)
print('basic02.py executed')