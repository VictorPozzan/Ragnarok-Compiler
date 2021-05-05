from index_terminals import index_ter
class Syntatic_Analyser :
    entrada = []
    pilha = [] 
    tabela = []

    def __init__(self, tokens):
        self.entrada = self.treat_list_tokens(tokens)

    def analyse(self):
        print("começou a Análise Sintática")
        print(self.entrada)
        
        table_production = Nao_Terminais()
        self.pilha.append("$")
        self.pilha.append("program")

        #print(self.pilha[-1])
        #pilha.pop();
        #var = "program"
        #print(getattr(table_production, var))
        
        for i in range(20):
            print("peração:", i)
            print("pilha:", self.pilha)
            print("entrada:", self.entrada)
            last_element_pilha = self.pilha[-1]
            if(last_element_pilha == self.entrada[0]): #ver se é um terminal
                print("Achei um terminal:", last_element_pilha)
                self.pilha.pop()
                self.entrada.pop(0)
                
            else:# encontra-se na pilha um não terminal
                print("Não terminal")
                index = index_ter[self.entrada[0]] #pegar o valor em index_terminals
                production = getattr(table_production, last_element_pilha)#acessar o objeto na lista
                print("production[index]",production[index])
                print("len:", len(production[index]))
                production = tuple(reversed((production[index]))) #inverte a tupla ("ID", "INT") -> ("INT", "ID")

                self.pilha.pop();
                self.insertInPilha(production)
                
                print("-1", self.pilha[-1])
                if self.pilha[-1] == ' ':
                    print("encontrei um vazio")
                    self.pilha.pop()
                    print("tirei o vazio:", self.pilha)
                
        #FITA-lista_tokens: MAIN { }
         #PILHA: program 
       
       
        #while self.list_tokens == '$':
            
    def insertInPilha(self, production):
        for prod in production:
            self.pilha.append(prod)
    
           
    
    def treat_list_tokens(self, tokens):
        lst_tokens = []
        terminal = ''

        for element in tokens:
            terminal = ''
            terminal = element[0][1:] #remove o primeiro caracter
            terminal = terminal[:-1] #remove o ultimo caracter
            lst_tokens.append(terminal)            
        
        lst_tokens.append('$') #adiciona o simbolo final da cadeia de produção
        return lst_tokens


class Nao_Terminais :
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
    caso_else = [ ("e"),("e"),(" ",),(" ",),("e"),(" ",),(" ",),(" ",),(" ",),("e"),("e"),(" ",),(" ",),(" ",),("else",),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e"),("e") ]
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







"""
"expr", "dv", "tipo", "inout", "input", "output", "de", "caso_else", "else"
                           "de_expr", "stmt", "stmt2", "atribuicao", "tipo_atribuicao", "possible_expr_atrib", "op_aritmetico",
                           "op_relacional", "op_logico_and_or", "op_logico_not", "valor"}
{
    id: 0
    v: 1
    ^: 2
    ¬: 3
    $: 4
}


lista_nao_terminais = [E, E', T, T', F]

E = [T E', erro, erro, T E', erro]
E' = []



lista_tokens = id v id ^


pilha = E(0)
pilha = TE'"""

