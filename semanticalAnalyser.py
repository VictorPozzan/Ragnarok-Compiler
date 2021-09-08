
class Semantic_Analyser:
    tokens = []
    tokens_deep = []
    list_var = []

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

        #print("------")
        #print(self.tokens_deep)
        #verificar atribuicoes
        self.verify_assignments()
        
        #verificar condicoes de if
        #verificar condicoes de while

    def insert_deep_structure(self):
        list_count_id = []
        count_id = 0
        list_count_id.append(count_id)
        lista= []
        for i, token in enumerate(self.tokens):
            self.tokens_deep.append((token[0], token[1], token[2], list_count_id[-1], list_count_id[0:]))
            
            if token[0] == '{{}':
                count_id = count_id + 1
                list_count_id.append(count_id)
            
            elif token[0] == '{}}':
                list_count_id.pop(-1)  

        
        
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
              
                if len(exists) == 1:
                    if token_receiver[2] >= exists[0][2] and exists[0][3] in token_receiver[4]:
                        # verificar se é uma atribição simples ou aritmetica {;} 
                        is_coma = self.tokens_deep[i + 2]
                        token_attributor = self.tokens_deep[i + 1]
                        if is_coma[0] == '{;}':
                            #verificar se for um id (se não for ele pode ser um INT_NUM, FLOAT_NUM, FALSE, TRUE)
                            self.verify_attributor(token_receiver, token_attributor)

                        else:
                            self.verify_attributor(token_receiver, token_attributor)
                            
                        
                        #se os identificadores foram declarados previamente 
                        #o id que vai receber é do mesmo tipo dos identificadores do outro lado

                    else: 
                        print("ERRROOO variavel utilizada fora de contexto", token_receiver[1])
                else:
                    errormessage = "variavel" + "'" + token_receiver[1] + "'" + "não foi declarada" 
                    self.printErro(errormessage, token[2])
                    
                    # ate encontar o {;} 
                        #se os identificadores foram declarados previamente 
                        #o id que vai receber é do mesmo tipo dos identificadores do outro lado


    def verify_type(self, token_receiver, token_attributor):
        if token_attributor[0] == "{ID}":
            type_attributor = list(filter(lambda x:token_receiver[1] in x, self.list_var))
        elif token_attributor[0] == "{NUM_INT}":
            type_attributor = [('{INT}')]
        elif token_attributor[0] == "{NUM_FLOAT}":
            type_attributor = [('{FLOAT}')]
        elif token_attributor[0] == "{FALSE}" or token_attributor[0] == "{TRUE}":
            type_attributor = [('{BOOL}')]
        else :
            type_attributor = [token_attributor[0]]

        type_receiver = list(filter(lambda x:token_receiver[1] in x, self.list_var))
        if type_receiver[0][0] == type_attributor[0][0]:
            return
        else:
            print("ERRO VARIAVEIS NAO SAO DO MESMO TIPO, ERA ESPERADO", type_receiver[0][0],  "E RECEBEMOS",  type_attributor[0], "linha", token_attributor[2])

    def verify_attributor(self, token_receiver, token_attributor):
        if token_attributor[0] == "{ID}":
        #verificar se este id esta declarado 
            exists_id_atributor = list(filter(lambda x:token_attributor[1] in x, self.list_var))
            if len(exists_id_atributor) == 1:
                if token_attributor[2] >= exists_id_atributor[0][2] and exists_id_atributor[0][3] in token_attributor[4]:
                    self.verify_type(token_receiver, token_attributor)
                else:
                    print("ERRROOO variavel utilizada fora de contexto", exists_id_atributor[1])
            else:
                print("ERRROOO id não declarado", exists_id_atributor[1])    
        else: 
            self.verify_type(token_receiver, token_attributor)
    

    def printErro(self, error, row, color_one = '\x1b[1;37;41m', color_two = '\x1b[0m'):
        a = 0
        #print(color_one, error, "       problema na linha ", row, color_two)