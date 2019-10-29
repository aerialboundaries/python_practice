import getch


class Hero(object):
    def __init__(self, x, y, is_movable, get_message, update):
        self.x = x
        self.y = y
        self.icon = '^'
        self.is_movable = is_movable
        self.get_message = get_message
        self.update = update

    def run(self):
        print('-----------------------------')
        print('w:up, a:left, s:right, z:down')
        print('ctrl-c: quit')
        print('-----------------------------')
        self.update()

        while(True):
            key = ord(getch.getch())
            if(key == 3):
                print('bye!!')
                break
            elif(key == 119):
                self.icon = '^'
                if(self.is_movable(self.x, self.y-1)):
                    self.y -= 1
            elif(key == 97):
                self.icon = '<'
                if(self.is_movable(self.x-1, self.y)):
                    self.x -= 1
            elif(key == 115):
                self.icon = '>'
                if(self.is_movable(self.x+1, self.y)):
                    self.x += 1
            elif(key == 122):
                self.icon = 'V'
                if(self.is_movable(self.x, self.y+1)):
                    self.y += 1
            elif(key == 100):
                self.talk()
                continue
            self.update()

    def talk(self):
        if(self.icon == '^'):
            message = self.get_message(self.x, self.y-1)
        elif(self.icon == '>'):
            message = self.get_message(self.x+1, self.y)
        elif(self.icon == '<'):
            message = self.get_message(self.x-1, self.y)
        elif(self.icon == 'V'):
            message = self.get_message(self.x, self.y+1)
        else:
            print('Error')
            exit()
        self.update(message)


class Townsman(object):
    def __init__(self, x, y, icon, message):
        self.x = x
        self.y = y
        self.icon = icon
        self.message = message


class Map(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.hero = Hero(3, 3, self.is_movable, self.get_message, self.update)
        self.townspeople = []
        self.townspeople.append(Townsman(3, 1, 'K', "I'm King"))
        self.townspeople.append(Townsman(1, 5, 'S', "I'm Soldier 1"))
        self.townspeople.append(Townsman(5, 5, 'S', "I'm Soldier 2"))

    def run(self):
        self.hero.run()

    def is_movable(self, x, y):
        if(x < 0):
            return False
        elif(self.width-1 < x):
            return False
        elif(y < 0):
            return False
        elif(self.height-1 < y):
            return False

        for townsman in self.townspeople:
            if(x == townsman.x and y == townsman.y):
                return False

        return True

    def update(self, message=''):
        characters = {}
        for townsman in self.townspeople:
            characters[(townsman.x, townsman.y)] = townsman.icon

        characters[(self.hero.x, self.hero.y)] = self.hero.icon

        def get_top_bottom_text():
            return '+' + '-' * self.width + '+\n'

        def get_message_border(width):
            return '#' * width + '\n'

        map_list = []
        map_list.append(get_top_bottom_text())
        for y in range(0, self.height):
            map_list.append('|')
            for x in range(0, self.width):
                if((x, y) in characters):
                    map_list.append(characters[(x, y)])
                else:
                    map_list.append(' ')
            map_list.append('|\n')
        map_list.append(get_top_bottom_text())
        map_list.append(get_message_border(10))
        map_list.append(message + '\n')
        map_list.append(get_message_border(10))
        print(''.join(map_list))

    def get_message(self, x, y):
        for townsman in self.townspeople:
            if(x == townsman.x and y == townsman.y):
                return townsman.message
        return 'no one exists..'


m = Map(7, 7)
m.run()
