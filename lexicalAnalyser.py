import re
from terminals import values

class Lexical_Analaser:
    tokens = []  # lista de tokens
    reserved_words = []
    symbols = []
    operators = []
    useless = []

    def __init__(self, program, reserved_words, symbols, operators, useless):  # construtor
        self.tokens = []
        self.program = program
        self.reserved_words = reserved_words
        self.symbols = symbols
        self.operators = operators
        self.useless = useless

    def analyse(self):
        print("Init Lexical Analyser")
        # print(self.program[0])

        row = 0
        for line in self.program:  # percorre a linha do programa
            row += 1
            col = 0
            line_character = line
            for i in range(len(line)):  # percorre caracter a caracter
                if i < col:
                    continue

                # verify if is it a ID or a reserved_word
                if line_character[i].isalpha():
                    word, col = self.word_analyse(line_character, i, col)
                    if word not in self.reserved_words:  # ID
                        self.tokens.append(("{ID}", word, row))
                    else:
                        for j in self.reserved_words:
                            if(j == word):
                                self.tokens.append(
                                    (values[word], word, row))

                # verify if it is a Digit
                elif line_character[i].isdigit():
                    type_number, number, col = self.number_analyse(
                        line_character, i, col)
                    if type_number != "erro":
                        self.tokens.append((type_number, number, row))
                    else:
                        self.lexical_error(row, col)

                # elif i in symbols:
                elif line_character[i] in self.symbols:
                    self.tokens.append(
                        (values[line_character[i]], line_character[i], row))
                    col += 1

                elif line_character[i] in self.operators:
                    # -, !, =
                    if line_character[i] == "-" and line_character[i+1].isdigit():
                        type_number, number, col = self.number_analyse(
                            line_character, i+1, col)
                        if type_number != "erro":
                            self.tokens.append((type_number, "-"+number, row))
                        else:
                            self.lexical_error(row, col)
                        col += 1
                    # if or "!" or "="
                    elif line_character[i] == "!" and line_character[i+1] == "=":
                        self.tokens.append(("{!=}", "!=", row))
                        col += 2
                    elif line_character[i] == "=" and line_character[i+1] == "=":
                        self.tokens.append(("{==}", "==", row))
                        col += 2
                    else:
                        self.tokens.append(
                            (values[line_character[i]], line_character[i], row))
                        col += 1
                # espaço, comentario, \n, \t
                elif line_character[i] in self.useless:
                    if line_character[i] == "#":
                        col = len(line)
                    else:
                        col += 1
                else:  # erro
                    self.lexical_error(row, col)
                    col += 1
     
        print('\x1b[6;30;42m',"Compiled Lexical Analyser :)", '\x1b[0m')
        
        return self.tokens

    def word_analyse(self, line_character, i, col):
        word = []
        while line_character[i].isalpha() or line_character[i].isalnum() or line_character[i] == "_":
            word.append(line_character[i])
            i += 1
            col += 1
        word_analysing = ''.join(word)
        return word_analysing, col

    def number_analyse(self, line_character, i, col):
        number_analysing = ""
        number = []
        while line_character[i].isdigit():
            number.append(line_character[i])
            i += 1
            col += 1

        if line_character[i] == ".":  # float
            number.append(line_character[i])
            i += 1
            col += 1

            if line_character[i].isdigit():
                while line_character[i].isdigit():
                    number.append(line_character[i])
                    i += 1
                    col += 1
                number_analysing = ''.join(number)
                return "{NUM_FLOAT}", number_analysing, col

            else:
                return "erro", number_analysing, col

        else:  # int
            number_analysing = ''.join(number)
            return "{NUM_INT}", number_analysing, col

    def lexical_error(self, row, col):
        print('\x1b[1;31;40m', "THERE IS A PROBLEM IN ROW: ", row, " COl: ", col, '\x1b[0m')


