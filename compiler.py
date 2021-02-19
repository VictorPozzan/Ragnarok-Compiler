from lexicalAnalyser import Lexical_Analaser

reserved_words = ["allr", "fljota", "aundan", "stund", "ef", "ella", "meioa", "lesa", "rita", "saor", "flar"]

symbols = ["{", "}", "(", ")", ";"]

operators = ["+", "-", "*", "/", "&", "|", "!", "<", ">", "!=", "==", "="]

useless = ["\n", "\t", "#", " "]


def main():
    program = open("./teste-2.vks", "r")

    print("Welcome to the Ragnarök compile for the language Vikings")
    print("Init compile the file", program.name)

    content_program = program.readlines()
    lexical = Lexical_Analaser(
        content_program, reserved_words, symbols, operators, useless)

    list_token = lexical.analyse()

    print(list_token)
    program.close()


if __name__ == "__main__":
    main()
