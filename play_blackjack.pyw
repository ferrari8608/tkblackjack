from cards import *
from players import *
from windows import *

def main():
    nameprompt = NamePrompt()
    playerid = nameprompt.player_id()
    mainwindow = GameWindow(playerid)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit()
