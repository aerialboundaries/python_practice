#!/usr/bin/env python
# Table printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidth = [0] * len(table)
    for i in colWidth:
        longestString = 0
        for j in range(len(table[i])):
            if len(table[i][j]) >= longestString:
                longestString = len(table[i][j])
        colWidth[i] = longestString

    longestWidth = 0
    for k in colWidth:
        if k >= longestWidth:
            longestWidth = k

    for lines in table:
        for items in lines:
            print(items.rjust(longestWidth + 2), end='')
        print('')

printTable(tableData)
