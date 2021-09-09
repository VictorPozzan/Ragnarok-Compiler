from lexicalAnalyser import Lexical_Analaser
from syntaticAnalyser import Syntatic_Analyser
from semanticalAnalyser import Semantic_Analyser
from ast import AbstractSintaxTree

reserved_words = ["allr", "fljota", "aundan", "stund", "ef", "ella", "meioa", "lesa", "rita", "saor", "flar"]

symbols = ["{", "}", "(", ")", ";"]

operators = ["+", "-", "*", "/", "&", "|", "!", "<", ">", "!=", "==", "="]

useless = ["\n", "\t", "#", " "]


def main():
    program = open("./teste-4.vks", "r")
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

    #Analisador Semantico
    semantic = Semantic_Analyser(list_token)
    errors, tokens = semantic.analyse()

    #if errors == 0:
    #ast = AbstractSintaxTree(tokens)
    #ast.execute()
    #else: 
    #    print("A AST não é infelizmente à ", errors, "erros a serem tratados ainda")


if __name__ == "__main__":
    print("Welcome to the Ragnarök compile for the language Vikings")
    main()
