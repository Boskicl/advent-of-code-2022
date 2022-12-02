import numpy as np

class RPC_Elf_Finder:
    def __init__(self, input_file: str) -> None:
        if isinstance(input_file, str):
            self.filename = input_file
        else:
            print("Error with input file type.") 
            return

    def file_reader(self) -> None:
        if not open(self.filename,"r"):
            print("Couldn't open file. Check extension.")
        else:
            with open(self.filename, "r") as f:
                return [line.strip().split() for line in f.readlines()]

    def game_on(self) -> int:
        df = self.file_reader()

        win_game = 6
        draw_game = 3
        lose_game = 0

        match = [win_game, draw_game, lose_game]

        score = {'X': 1,'Y': 2,'Z': 3}

        d = {
            'A': ['Y', 'X', 'Z'],
            'B': ['Z', 'Y', 'X'],
            'C': ['X', 'Z', 'Y']
        }

        d2 = {
            'X': lose_game,
            'Y': draw_game,
            'Z': win_game
        }

        part1 = 0
        part2 = 0
        for a, b in df:
            part1 += score[b] + match[d[a].index(b)]
            part2 += d2[b] + score[d[a][match.index(d2[b])]]
            
        return part1,part2

if __name__ == '__main__':
    input_file = "inputfile.txt"
    RPC = RPC_Elf_Finder(input_file)
    part1,part2 = RPC.game_on()

    print(part1)
    print(part2)