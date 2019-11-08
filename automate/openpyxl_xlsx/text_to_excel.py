import glob

import openpyxl


wb = openpyxl.Workbook()
ws = wb.active
tFiles = glob.glob('*.txt')
print(tFiles)
for x, tFile in enumerate(tFiles, 1):
    with open(tFile, 'r') as f:
        for y, line in enumerate(f, 1):
            ws.cell(row=y, column=x).value = line
wb.save('test_to_excel.xlsx')
