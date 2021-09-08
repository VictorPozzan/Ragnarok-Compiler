
class Semantic_Analyser:
    tokens = []
    tokens_deep = []
    list_var = []
    count_id = 0
    list_count_id = []
    list_ID_context = []


    def __init__(self, tokens):
        self.tokens = tokens
        self.count = 0
    
    def analyse(self):
        print("init semantic analyser")
        #inert the deep structure in tokens
        self.insert_deep_structure()

        #construct the variable table
        self.construct_variable_table()

        #verificar variaveis inuteis
        self.useless_var()

        print("------")
        print(self.list_var)
        #verificar atribuicoes
        self.verify_assignments()
        
        #verificar condicoes de if
        #verificar condicoes de while

    def insert_deep_structure(self):
        self.list_count_id.append(self.count_id)
        for i, token in enumerate(self.tokens):
            #print(token)
            if token[0] == '{{}':
                self.count_id = self.count_id + 1
                self.list_count_id.append(self.count_id)
            
            elif token[0] == '{}}':
                self.list_count_id.pop(-1)  
            self.tokens_deep.append((token[0], token[1], token[2], self.list_count_id[-1]))


    def construct_variable_table(self):
        for i, token in enumerate(self.tokens_deep):
            if token[0] == '{INT}' or token[0] == '{FLOAT}' or token[0] == '{BOOL}':
                next_token =  self.tokens_deep[i + 1]

                #verificar se não esta na lista
                exists = list(filter(lambda x:next_token[1] in x, self.list_var))
                if len(exists) > 0:
                    errormessage =  "variavel " + "'" + next_token[1] +"'"+ " já foi declarada"
                    self.printErro( errormessage,  next_token[2])
                else:
                    #ex: struct of tuple lis_var (type, value, row, id_structure)
                    self.list_var.append((token[0], next_token[1], token[2], token[3]))
    

    def useless_var(self):
        for i, token in enumerate(self.list_var):
            name_var = token[1]
            useless = list(filter(lambda x:name_var in x, self.tokens))
            if len(useless) == 1:
                errormessage = "variavel" + "'" + name_var + "'" + "foi declarada mas nunca utilizada" 
                self.printErro(errormessage, token[2], '\x1b[1;37;33m')


    def verify_assignments(self):
        for i, token in enumerate(self.tokens_deep):
            if token[0] == '{=}':
                #verificar se o id que recebe foi declarado previamente
                token_receiver = self.tokens_deep[i - 1]
                exists = list(filter(lambda x:token_receiver[1] in x, self.list_var))
                print('exists', exists)
                if len(exists) == 1:
                    if token_receiver[2] >= exists[0][2] and token_receiver[3] >= exists[0][3]:
                        print("next step")
                    else: 
                        print("variavel utilizada fora de contexto")
                else:
                    errormessage = "variavel" + "'" + token_receiver[1] + "'" + "não foi declarada" 
                    self.printErro(errormessage, token[2])
                    
                    # ate encontar o {;} 
                        #se os identificadores foram declarados previamente 
                        #o id que vai receber é do mesmo tipo dos identificadores do outro lado


    def printErro(self, error, row, color_one = '\x1b[1;37;41m', color_two = '\x1b[0m'):
        print(color_one, error, "       problema na linha ", row, color_two)