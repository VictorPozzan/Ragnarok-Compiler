

class Syntatic_Analyser :
    list_tokens = []
    #pilha 
    tabela = []

    def __init__(self, tokens):
        self.list_tokens = self.treat_list_tokens(tokens)

    def analyse(self):
        print("começou a Análise Sintática")
        print(self.list_tokens)
        
        var = "a";
        listas = Nao_Terminais()
        
        print(getattr(listas, var))
        
       #FITA-lista_tokens: MAIN { }
       #PILHA: program 
       
       
        #while self.list_tokens == '$':
            
        
        
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


class Nao_Terminais:
    program = [("a", "b")]
    main = [("erro"), ("erro")]
    possible_expr = [("atribuicao"),("ID")]
    b = [("c","h")]
    a = [("k, l")]
    

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

