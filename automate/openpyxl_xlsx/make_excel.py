import random
from openpyxl import Workbook


for i in range(1, 6):

    wb = Workbook()

    for j in range(5):
        ws = wb.create_sheet()

    for x, ws in enumerate(wb, 1):
        ws.title = ('sheet' + str(x).zfill(3))
        for row in range(1, 40):
            ws.append([100*random.random() for _ in range(10)])

    wb.save('book' + str(i).zfill(2) + '.xlsx')
