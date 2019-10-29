# -*- coding: utf-8 -*-

import csv
with open('roboter.csv', 'w+', newline = '') as csv_file:
    fieldnames = ["NAME", "COUNT"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames) 
    writer.writeheader()

    while True:
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)
        restlist = [row for row in reader]
        print(reader)
        print("こんにちは、私の名前はRobokoです。あなたの名前は何ですか")  
        username = input()
        
        if restlist is not None:    
            restlist.sort(key=lambda x: x["COUNT"], reverse=True)   
            
            for recom in restlist:
                print("私のお勧めのレストランは{}です。\nこのレストランは好きですか？\
                [Yes/No]".format(recom["NAME"]))
        
                yn = input()
                    
                if yn in ['Y', 'y', 'Yes', 'yes']:
                    recom["COUNT"] += 1
                    break
                elif yn in ['N', 'n', 'No', 'no']:
                    continue
                else:
                    print("YesかNoで答えて下さい。")
                    continue
        
        print(username + "さん、どこのレストランが好きですか？")
        favorite = input()
        
        if favorite not in restlist:
            restlist.append({"NAME": favorite, "COUNT": 0})
        
        for rest in restlist:
            if favorite in rest:
                rest["COUNT"] += 1

        print(restlist)

        writer.writerows(restlist)

       
        print(username + "さん。ありがとうございました。\n良い一日を！　さようなら。\n\n")
