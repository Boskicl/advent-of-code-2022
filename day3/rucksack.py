import numpy as np

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

    def start(self) -> int:
        all_ruckstacks = self.file_reader()
        all_ruckstacks[0:5]

        for ruckstack in all_ruckstacks:
            print(ruckstack)
            # split each "ruckstack" in two equal halves
            compartment1, compartment2 = ruckstack[:len(ruckstack)//2] , ruckstack[len(ruckstack)//2:]
            print(compartment1)
            print(compartment2)



if __name__ == '__main__':
    input_file = "inputfile.txt"
    RPC = Elf_Rucksack(input_file)
    RPC.start()
