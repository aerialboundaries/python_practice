import csv


class Roboter():

    def __init__(self, name):
        self.name = name

    def get_user_name(self):
        print("\nこんにちは！　私は{}です。あなたの名前は何ですか？".format(self.name))
        user_name = input()
        user_name = user_name.title()
        return user_name

    def recommendation(self, recommend):
        print("\n私のオススメのレストランは、{}です。".format(recommend))
        print("このレストランは好きですか？[Yes/No]")

        while True:
            answer = input()
            if answer in ['Yes', 'yes', 'Y', 'y']:
                favorite = True
                break
            elif answer in ['No', 'no', 'N', 'n']:
                favorite = False
                break
            else:
                print("YesかNoで答えてください")
                continue

        return favorite

    def get_new_restaurant(self, user_name):
        print("\n{}さん。どこのレストランが好きですか？".format(user_name))
        new_restaurant = input()
        new_restaurant = new_restaurant.title()
        return new_restaurant

    def greetings(self, user_name):
        print("\n{}さん。ありがとうございました。".format(user_name))
        print("良い一日を!　さようなら。\n")


with open('roboter.csv', 'w+', newline='') as csv_file:
    fieldnames = ['NAME', 'COUNT']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

roboko = Roboter('Roboko')

for _ in range(5):
    with open('roboter.csv', 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        restaurant_list = [row for row in reader]
        restaurant_list.sort(key=lambda x: x['COUNT'], reverse=True)

    user_name = roboko.get_user_name()

    if restaurant_list:
        for i in restaurant_list:
            recommend = i['NAME']
            if roboko.recommendation(i['NAME']) == True:
                s = i['COUNT']
                s = int(s) + 1
                i['COUNT'] = s
                break

    new_restaurant = roboko.get_new_restaurant(user_name)
    exist = False
    for i in restaurant_list:
        if i['NAME'] == new_restaurant:
            s = i['COUNT']
            s = int(s) + 1
            i['COUNT'] = s
            exist = True

    if exist == False:
        restaurant_list.append({'NAME': new_restaurant, 'COUNT': 1})

    with open('roboter.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(restaurant_list)

    roboko.greetings(user_name)
