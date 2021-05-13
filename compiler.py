from lexicalAnalyser import Lexical_Analaser
from syntaticAnalyser import Syntatic_Analyser

reserved_words = ["allr", "fljota", "aundan", "stund", "ef", "ella", "meioa", "lesa", "rita", "saor", "flar"]

symbols = ["{", "}", "(", ")", ";"]

operators = ["+", "-", "*", "/", "&", "|", "!", "<", ">", "!=", "==", "="]

useless = ["\n", "\t", "#", " "]


def main():
    program = open("./teste-2.vks", "r")
    print("Init compile the file", program.name)
    content_program = program.readlines()

    #Analisador Léxico
    lexical = Lexical_Analaser(
        content_program, reserved_words, symbols, operators, useless)
    list_token = lexical.analyse()
    #print(list_token)
    program.close()

    #Analisador Sintático
    syntatic = Syntatic_Analyser(list_token)
    syntatic.analyse()


if __name__ == "__main__":
    print("Welcome to the Ragnarök compile for the language Vikings")
    main()
