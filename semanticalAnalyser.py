
class Semantic_Analyser:
    tokens = []
    list_var = []
    count_id = 0
    list_count_id = []

    def __init__(self, tokens):
        self.tokens = tokens
        self.count = 0
    
    def analyse(self):
        print("init semantic analyser")
        #construct the variable table
        self.construct_variable_table()
        print("------")
        print(self.list_var)
        #verificar variaveis inuteis
        self.useless_var()
        #verificar atribuicoes
        #verificar condicoes de if
        #verificar condicoes de while

    def construct_variable_table(self):
        for i, token in enumerate(self.tokens):
            #print(token)
            if token[0] == '{{}':
                self.count_id = self.count_id + 1
                self.list_count_id.append(self.count_id)
            
            elif token[0] == '{}}':
              self.list_count_id.pop(-1)  

            elif token[0] == '{INT}' or token[0] == '{FLOAT}' or token[0] == '{BOOL}':
                next_token =  self.tokens[i + 1]
                #verificar se não esta na lista
                    
                exists = list(filter(lambda x:next_token[1] in x, self.list_var)) 
                if len(exists) > 0:
                    errormessage =  "variavel " + "'" + next_token[1] +"'"+ " já foi declarada"
                    self.printErro( errormessage,  next_token[2])
                else:
                    #ex: struct of tuple lis_var (type, value, row, id_structure)
                    self.list_var.append((token[0], next_token[1], token[2], self.list_count_id[-1]))
    
    def useless_var(self):
        for i, token in enumerate(self.list_var):
            name_var = token[1]
            useless = list(filter(lambda x:name_var in x, self.tokens))
            if len(useless) == 1:
                errormessage = "variavel" + "'" + name_var + "'" + "foi declarada mas nunca utilizada" 
                self.printErro(errormessage, token[2], '\x1b[1;37;33m')

    def printErro(self, error, row, color_one = '\x1b[1;37;41m', color_two = '\x1b[0m'):
        print(color_one, error, "       problema na linha ", row, color_two)