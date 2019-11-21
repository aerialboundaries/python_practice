import pathlib
import csv
import pprint

import openpyxl.workbook


# Make a directory for the generated csv files.
csv_path = pathlib.Path('C:/home/practice/python/automate/csv/from_excel')
csv_path.mkdir(exist_ok=True)
excellist = list(pathlib.Path('C:/home/practice/python/automate/'
                              'openpyxl_xlsx').glob('*.xlsx'))
# pprint.pprint(excellist)

# For each excel file, for each sheet, write csv
for wbfile in excellist:
    wb = openpyxl.load_workbook(wbfile)
    basefile = pathlib.Path(wbfile).stem
    for ws in wb:
        with open(csv_path.joinpath(basefile + '_' + ws.title + '.csv'),
                  'w', newline='') as f:
            csvWriter = csv.writer(f)
            # for row in ws.values:
            #     csvWriter.writerow(row)
            csvWriter.writerows(ws.values)
