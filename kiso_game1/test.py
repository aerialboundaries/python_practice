import getch

class Hero:
    def run(self):
        while(True):
            key = ord(getch.getch())
            if(key == 3): # Ctrl-C: Quit
                print('bye!!')
                break;
            print('key input: ' + str(key))

hero = Hero()
hero.run()
