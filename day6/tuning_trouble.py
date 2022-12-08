import re

class Elf_sorter:
    def __init__(self, input_file: str) -> None:
        if isinstance(input_file, str):
            self.filename = input_file
        else:
            print("Error with input file type.") 
            return

    def file_reader(self) -> None:
        with open(self.filename,"r") as f:
            df = f.read().splitlines()
        return df
    
    def location_string(self,df,length):
        for i in range(0,len(df)):
            chunk = df[i:i+length]
            if len(set(chunk)) == length:
                return i+length
        return -1

    def runner(self):
        df = self.file_reader()[0]
        start_packet = self.location_string(df,4)
        start_message = self.location_string(df,14)

        print(start_packet)
        print(start_message)
        
        
if __name__ == '__main__':
    input_file = "inputfile.txt"
    RPC = Elf_sorter(input_file)
    ans = RPC.runner()
