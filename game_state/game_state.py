
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class GameState:

    class GameKey:
        def __init__(self, filename):
            self.key = []
            opened = open(filename, 'r')
            lines = opened.readlines()
            for line in lines:
                row = []
                for ch in line.strip():
                    row.append(ch)
                self.key.append(row)
            print(self.key)
            return

        def __repr__(self) -> str:
            ret_str = ''
            for row in self.key:
                for ch in row:
                    if ch == 'b':
                        ret_str += f"{bcolors.OKBLUE}b "
                    elif ch == 'x':
                        ret_str += f"{bcolors.OKBLUE}x "
                    elif ch == 'r':
                        ret_str += f"{bcolors.FAIL}f "
                    else:
                        ret_str += f"{bcolors.OKGREEN}. "
                ret_str += "\n"
            return ret_str



    def __init__(self, gamekey_file):
        self.gk = self.GameKey(gamekey_file)
        print(self.gk)
        pass


if __name__ == "__main__":
    gs = GameState("../gamekey.txt")