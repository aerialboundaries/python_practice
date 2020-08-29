import re

numRegex = re.compile(r'^\d{1,3}(,\d{3})*$')
testnum = ['42', '1,234', '6,368,745', '12,34,567', '1234']
for i in testnum:
    mo = numRegex.search(i)
    if mo != None:
        print(mo.group())
    else:
        print(str(i) + ' is not correct.')
