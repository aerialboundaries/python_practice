import csv


header = ['Header', 'Header', 'Header', 'Header', 'Header']
baselist = ['1', '2', '3', '4', '5']
for i in range(1, 11):
    with open('test{:0>2}.csv'.format(str(i)), 'w', newline='') as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(header)
        for j in range(1, i+1):
            content = [x * j for x in baselist]
            csvWriter.writerow(content)
