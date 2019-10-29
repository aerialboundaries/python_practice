# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:45:43 2019

@author: mtakatani
"""

class Roboter():
    
    username = ''
    
    def __init__(self, name):
        
        self.name = name
        
        import csv
        
        with open(name + '.csv', 'w', encoding='utf8', newline = '') as csv_file:
            writer = csv.DictWriter(csv_file, ['NAME', 'COUNT'])
            writer.writeheader()            

    def greetings1(self):
        print("こんにちは、私の名前は" + self.name + "です。あなたの名前は何ですか")  
        username = input()
        
    def question(self):
        print(username + "さん、どこのレストランが好きですか？")
        
    
    def recommendation(self):
        import csv
        with open(self.name + '.csv', 'r+', newline = '') as csv_file:
            reader = csv.DictReader(csv_file)
            restlist = [row for row in reader]
            recomlist = sorted(restlist, key=lambda x: x['COUNT'], reverse=True)
            
            for recom in recomlist:
                print("私のお勧めのレストランは{}です。\nこのレストランは好きですか？\
                         [Yes/No]".format(recom['NAME']))
    
                yn = input()
                    
                if yn in ['Y', 'y', 'Yes', 'yes']:
                    recom['NAME'] += 1
                    break
                elif yn in ['N', 'n', 'No', 'no']:
                    continue
                else:
                    print("YesかNoで答えて下さい。")
                    continue
                
            writer = csv.DictWriter(csv_file)
            writer.writerows(recomlist)
            
    def greetings2(self, username):
        print(username + "さん。ありがとうございました。\n 良い一日を！　さようなら。")
        
        
            
            
                
            