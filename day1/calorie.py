import numpy as np

class Calorie_Elf_Finder:
    def __init__(self,input_file):
        if isinstance(input_file, str):
            self.filename = input_file
        else:
            print("Error with input file type.")

    def file_reader(self):
        if not open(self.filename,"r"):
            print("Couldn't open file. Check extension.")
        else:
            with open(self.filename, "r") as f:
                return f.read()

    def findMaxCalElf(self):
        f = self.file_reader()
        total_calories_of_all_elves = []
        for indv_elf in f.split("\n\n"):
            total_calories_of_elf= np.fromstring(indv_elf, dtype=np.int_, sep="\n").sum()
            total_calories_of_all_elves.append(total_calories_of_elf)
        total_calories_of_all_elves.sort()
        return total_calories_of_all_elves[-1:]


C = Calorie_Elf_Finder("inputfile.txt")
print("Max total calories being carried by an elf: {0}".format(C.findMaxCalElf()))