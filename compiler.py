from lexicalAnalyser import Lexical_Analaser

reserved_words = ["allr", "fljota", "bref", "aundan", "stund",
                  "ef", "ella", "meioa", "lesa", "rita", "saor", "flar"]

symbols = ["{", "}", "(", ")", ";", "#", "="]

operators = ["+", "-", "*", "/", "&", "|", "!", "<", ">", "!=", "=="]


def main():
    program = open("./teste-1.vks", "r")

    print("Welcome to the Ragnarök compile for the language Vikings")
    print("Init compile the file", program.name)

    content_program = program.readlines()
    lexical = Lexical_Analaser(
        content_program, reserved_words, symbols, operators)

    lexical.analyse()

    program.close()


if __name__ == "__main__":
    main()
