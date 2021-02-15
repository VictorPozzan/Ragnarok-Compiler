

class Lexical_Analaser:
    tokens = []  # lista de tokens
    reserved_words = []
    symbols = []
    operators = []

    def __init__(self, program, reserved_words, symbols, operators):
        self.program = program

    def analyse(self):
        print("Init analyse the lexical part")
        print(self.program[0])

        for line in self.program:
            # print(line)
            print(line)
