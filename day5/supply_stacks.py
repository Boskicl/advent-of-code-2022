import re

class Elf_sorter:
    def __init__(self, input_file: str) -> None:
        if isinstance(input_file, str):
            self.filename = input_file
        else:
            print("Error with input file type.") 
            return

    def file_reader(self) -> None:
        df = []
        with(open(self.filename,"r")) as f:
            for line in f:
                df.append(line)
        return df
    
    def runner(self):
        instructions = [[]]
        crates = []
        crate_stacks = []
        procedure = []

        df = self.file_reader()

        for line in df:
            if line == '\n':
                instructions.append([])
            elif line != '\n':
                instructions[-1].append(line.split('\n')[0])

        drawning = instructions[0]
        for line in drawning:
            crates.append([line[containers * 4 + 1] for containers in range(len(line) // 4 + 1)]) 
        crate_stacks = [list("".join(stack_column).strip()[::-1]) for stack_column in zip(*crates)]
        for step in instructions[1]:
            step = step.split(' ')
            step.remove('move')
            step.remove('from')
            step.remove('to')
            procedure.append(step)

        for step in procedure:
            times = int(step[0])
            start = int(step[1])
            end = int(step[2])

            i = times
            while i > 0:
                # crate = crate_stacks[start-1].pop() # part1
                crate = crate_stacks[start-1].pop(len(crate_stacks[start-1]) - i) # part2
                crate_stacks[end-1].append(crate)
                i = i-1

        top = ""
        for i in range(len(crate_stacks)):
            top = "".join([top,crate_stacks[i].pop()])
            
        # print answer
        print(top)

        
if __name__ == '__main__':
    input_file = "inputfile.txt"
    RPC = Elf_sorter(input_file)
    ans = RPC.runner()
