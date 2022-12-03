import string

class Elf_Rucksack:
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
                return [l.strip('\n') for l in f.readlines()]

    def part1(self) -> int:
        asciiLetters = string.ascii_letters
        all_ruckstacks = self.file_reader()

        sum_priorities = 0

        for ruckstack in all_ruckstacks:
            # print(ruckstack)
            # split each "ruckstack" in two equal halves
            compartment1, compartment2 = ruckstack[:len(ruckstack)//2] , ruckstack[len(ruckstack)//2:]
            # print(compartment1)
            # print(compartment2)
            common_letters = set(compartment1).intersection(set(compartment2))
            sum_priorities += asciiLetters.index(common_letters.pop()) + 1
        return sum_priorities



if __name__ == '__main__':
    input_file = "inputfile.txt"
    RPC = Elf_Rucksack(input_file)
    part1 = RPC.part1()
    # part2 = RPC.part2()

    print("Answer part 1: {}".format(part1))
    # print("Answer part 2: {}".format(part2))
