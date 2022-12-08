import string

class Elf_sorter:
    def __init__(self, input_file: str) -> None:
        if isinstance(input_file, str):
            self.filename = input_file
        else:
            print("Error with input file type.") 
            return

    def file_reader(self) -> None:
        df = []
        if not open(self.filename,"r"):
            print("Couldn't open file. Check extension.")
        else:
            with open(self.filename, "r") as f:
                for line in f:
                    line = line.strip()
                    df.append(line.split(','))
            return df

    
    def part1(self):
        # pairs with overlapping ranges 
        counter = 0
        df = self.file_reader()
        for pair in df:
            elf1, elf2 = pair[0],pair[-1]
            elf1_start, elf1_end = elf1.split("-")
            elf2_start, elf2_end = elf2.split("-")
            
            elf1_start = int(elf1_start)
            elf1_end = int(elf1_end)
            elf2_start = int(elf2_start)
            elf2_end = int(elf2_end)

            if (elf1_start <= elf2_start) and (elf1_end >= elf2_end):
                counter+=1
            elif (elf2_start <= elf1_start) and (elf2_end >= elf1_end):
                counter+=1
        return counter


        return 0

    def part2(self):
        # Overlapping pairs
        counter = 0
        df = self.file_reader()
        for pair in df:
            elf1, elf2 = pair[0],pair[-1]
            elf1_start, elf1_end = elf1.split("-")
            elf2_start, elf2_end = elf2.split("-")
            
            elf1_start = int(elf1_start)
            elf1_end = int(elf1_end)
            elf2_start = int(elf2_start)
            elf2_end = int(elf2_end)

            if (elf1_start <= elf2_start) and (elf1_end >= elf2_start):
                counter+=1
            elif (elf2_start <= elf1_start) and (elf2_end >= elf1_start):
                counter+=1
        return counter


        return 0


if __name__ == '__main__':
    input_file = "inputfile.txt"
    RPC = Elf_sorter(input_file)
    part1 = RPC.part1()
    part2 = RPC.part2()

    print("Answer part 1: {}".format(part1))
    print("Answer part 2: {}".format(part2))
