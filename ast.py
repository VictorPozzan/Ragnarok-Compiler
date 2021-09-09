class AbstractSintaxTree:
    tokens = []
    new_tokens = []
    id = 0
    count = 0
    actual_list = []
    
    def __init__(self, tokens):
        self.tokens = tokens

    def execute(self):
        print("INIT  AST")
        #for i, token in enumerate(self.tokens):
        #    self.new_tokens.append((token[0], token[1], token[2], self.id))
        #    self.id = self.id + 1 
        
        #print(self.new_tokens)
        print(self.tokens)
        tree = []
        self.actual_list.append(("main", "{", [], "}"))
        self.count = 2
        self.recursive_tree(self.actual_list, self.tokens)

        print("treeeeeeeee")    
        print(self.actual_list)
    
    def recursive_tree(self, tree, tokens):
        for i, token in enumerate(tokens):
            #declaracao de var
            deep = token[3]
            print( self.actual_list)
            if token[0] == '{FLOAT}' or token[0] == '{INT}' or token[0] == '{BOOL}':
                print("declaracao de var")
                print(self.actual_list[0])
                self.actual_list[0][self.count].append(("var_declaration:", token[0]))
            
            if token[0] == '{=}':
                print("atibuttion")

            if token[0] == '{IF}':
                print("if")
                self.actual_list[0][self.count].append(("IF", "(", [], ")", "{", [], '}'))
                lista = self.actual_list[0][2][1]
                print("lista")
                print(lista)
                self.count = 5;
                self.actual_list = [lista]

            if token[0] == '{ELSE}':
                print("else")

            if token[0] == '{WHILE}':
                print("while")

#declarao variaveis int ->
#atribuicao de var   a = b   a = b + 1
#if -> child ( stmt )
#while -> child  ( stmt )
#else - > { stmt }
#print -> ( ID )
#scan
            