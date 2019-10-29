# -*- coding: utf-8 -*-

import csv
with open('roboter.csv', 'w', newline = '') as csv_file:
    fieldnames = ['NAME', 'COUNT']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames) 
    writer.writeheader()

while True:
    with open('roboter.csv', 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        restlist = [row for row in reader]
        print(restlist)
        print("こんにちは、私の名前はRobokoです。あなたの名前は何ですか")  
        username = input()
        
        if restlist is not None:    
            restlist.sort(key=lambda x: x['COUNT'], reverse=True)   
            
            for recom in restlist:
                print("私のお勧めのレストランは{}です。\nこのレストランは好きですか？\
                [Yes/No]".format(recom['NAME']))
        
                yn = input()
                    
                if yn in ['Y', 'y', 'Yes', 'yes']:
                    recom['COUNT'] += 1
                    break
                elif yn in ['N', 'n', 'No', 'no']:
                    continue
                else:
                    print("YesかNoで答えて下さい。")
                    continue
        
        print(username + "さん、どこのレストランが好きですか？")
        favorite = input()
        
        if favorite not in restlist:
            restlist.append({'NAME': favorite, 'COUNT': 0})
        
        print(restlist)

    with open('roboter.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader
        writer.writerows(restlist)
        print(restlist)

        
    print(username + "さん。ありがとうございました。\n良い一日を！　さようなら。\n\n")
