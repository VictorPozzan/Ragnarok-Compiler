from index_terminals import index_ter
class Syntatic_Analyser :
    FAIL = '\033[91m',
    ENDC = '\033[0m',
    entrada = []
    pilha = [] 
    tabela = []
    row = []

    def __init__(self, tokens):
        self.entrada, self.row = self.treat_list_tokens(tokens)

    def analyse(self):
        print('\n')
        print("Init Syntatical Analyser")
        #print('\n')
        #print(self.entrada)
        
        table_production = Nao_Terminais()
        self.pilha.append("$")
        self.pilha.append("program")

        last_token = 'was expected the word "meioa"'
        
        while self.pilha[-1] != '$' and self.entrada[0] != '$':
            #print("\n")
            #print("pilha:", self.pilha)
            #print("entrada:", self.entrada)
            last_element_pilha = self.pilha[-1]
           
            if last_element_pilha in index_ter: #fazer a verificação se é um teminal 
                if(last_element_pilha == self.entrada[0]): #se o topo da pilha é igual ao top da entrada
                    self.pilha.pop()
                    last_token = " after: " + str(self.entrada[0])
                    self.entrada.pop(0) #não desempilhar criar um contador pra sentença toda vez que cair aqui dar um ++ no contador    
                    self.row.pop(0)
                else:
                    print('\x1b[1;37;41m', "Type 1: ERROR was expected a ", self.pilha[-1] , " on line:", self.row[0], last_token, '\x1b[0m')
                    self.pilha.pop()          
            else:# encontra-se na pilha um não terminal
                index = index_ter[self.entrada[0]] #pegar o valor em index_terminals 
                

                production = getattr(table_production, last_element_pilha)
                #print("production[index]",production[index])
                production = tuple(reversed((production[index]))) #inverte a tupla ("ID", "INT") -> ("INT", "ID")
                
                if production[0] == 'e':
                    print('\x1b[1;37;41m', "Type 2: ERROR was expected a ", self.pilha[-1], " on line:", self.row[0], '\x1b[0m')
                    self.pilha.pop();
                else:
                    self.pilha.pop();
                    self.insertInPilha(production)
              
                if self.pilha[-1] == ' ':
                    self.pilha.pop()
                    
        print('\x1b[6;30;42m',"Compiled Syntatical Analyser :)", '\x1b[0m')

            
    def insertInPilha(self, production):
        for prod in production:
            self.pilha.append(prod)
    
           
    
    def treat_list_tokens(self, tokens):
        lst_tokens = []
        lst_row = []
        terminal = ''

        for element in tokens:
            terminal = ''
            lst_row.append(element[2])
            terminal = element[0][1:] #remove o primeiro caracter
            terminal = terminal[:-1] #remove o ultimo caracter
            lst_tokens.append(terminal)            
        
        lst_tokens.append('$') #adiciona o simbolo final da cadeia de produção
        return lst_tokens, lst_row


class Nao_Terminais :
    #modifica os nome input -> put e else -> els
    program = [("main",),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e")]			
    main = [ ("MAIN", "{", "possible_expr", "}"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]		
    possible_expr = [ ("e"),("e"), (" ",), ("expr", "possible_expr"),("e"),("expr", "possible_expr"),("expr", "possible_expr"),("expr", "possible_expr"),("expr", "possible_expr"),("e"),("e"),("expr", "possible_expr"),("expr", "possible_expr"),("expr", "possible_expr"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]
    expr = [ ("e"),("e"),("e"),("atribuicao",),("e"),("dv",),("dv",),("dv",),("inout",),("e"),("e"),("inout",),("de",),("de",),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]			
    dv = [ ("e"),("e"),("e"),("e"),("e"),("tipo", "ID", ";"),("tipo", "ID", ";"),("tipo", "ID", ";"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]
    tipo = [ ("e"),("e"),("e"),("e"),("e"),("INT",),("FLOAT",),("BOOL",),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]
    inout = [ ("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("put",),("e"),("e"),("output",),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]			
    put = [ ("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("SCAN", "(", "ID", ")", ";"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]		
    output = [ ("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("PRINT", "(", "ID", ")", ";"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e")	]	
    de = [ ("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("IF", "(", "stmt", ")", "de_expr", "caso_else"),("WHILE", "(", "stmt", ")", "de_expr"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]
    caso_else = [ ("e"),("e"),(" ",),(" ",),("e"),(" ",),(" ",),(" ",),(" ",),("e"),("e"),(" ",),(" ",),(" ",),("els",),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]
    els = [ ("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("ELSE", "de_expr"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]
    de_expr = [ ("e"),("{", "possible_expr", "}"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]
    stmt = [ ("e"),("e"),("e"),("valor", "op_relacional", "valor", "stmt2"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("op_logico_not", "valor"),("valor", "op_relacional", "valor", "stmt2"),("valor", "op_relacional", "valor", "stmt2"),("valor", "op_relacional", "valor", "stmt2"),("valor", "op_relacional", "valor", "stmt2")	]
    stmt2 = [ ("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),(" ",),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("op_logico_and_or", "valor", "op_relacional", "valor"),("op_logico_and_or", "valor", "op_relacional", "valor"),("e"),("e"),("e"),("e"),("e") ]	
    atribuicao = [ ("e"),("e"),("e"),("ID", "=", "tipo_atribuicao", ";"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]		
    tipo_atribuicao = [ ("e"),("e"),("e"),("valor", "possible_expr_atrib"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("valor", "possible_expr_atrib"),("valor", "possible_expr_atrib"), ("valor", "possible_expr_atrib"),("valor", "possible_expr_atrib") ]			
    possible_expr_atrib = [ ("e"),("e"),("e"),("e"),(" ",),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("op_aritmetico", "valor"),("op_aritmetico", "valor"),("op_aritmetico", "valor"),("op_aritmetico", "valor"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]			
    op_aritmetico = [ ("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("+",),("-",),("/",),("*",),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]			
    op_relacional = [ ("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("==",),("!=",),("LESS",),("MORE",),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]	
    op_logico_and_or = [ ("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("AND",),("OR",),("e"),("e"),("e"),("e"),("e") ]
    op_logico_not = [ ("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("NOT",),("e"),("e"),("e"),("e") ]
    valor = [ ("e"),("e"),("e"),("ID",),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("NUM_INT",),("NUM_FLOAT",),("FALSE",),("TRUE",) ]
