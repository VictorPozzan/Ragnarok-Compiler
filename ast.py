

class AbstractSintaxTree:
    tokens = []
    new_tokens = []
    id = 0
    count = 0
    actual_list = []

    def __init__(self, tokens):
        self.tokens = tokens

    def execute(self):
        tab = 1
        file = open("ast", "w")
        file.write("Program { \n")

        file.write((tab * "\t") + "body: [ \n")
        for i, token in enumerate(self.tokens):
            if i != len(self.tokens) - 1:
                next_token = self.tokens[i + 1]
            
            if token[0] == '{INT}' or token[0] == '{FLOAT}' or token[0] == '{BOOL}':
                self.variableDeclaration(file, token, next_token, tab)
            
            if token[0] == '{PRINT}' or token[0] == '{SCAN}':
                id_token = self.tokens[i + 2]
                self.inputOutputDeclaration(file, token, id_token, tab)

            if token[0] == '{ID}' and next_token[0] == '{=}':
                self.expressionStatement(file, token, i, tab)
            
            if token[0] == '{WHILE}':
                self.whileStatemente(file, token, i, tab)
                tab = tab + 3

            if token[0] == '{}}' and i !=  len(self.tokens) - 1:
                tab = tab - 3
                self.closeBody(file, token, i, tab)

            #if token[0] == '{IF}':
            #if token[0] == '{ELSE}'    



        file.write((tab * "\t") + "] \n" )
        file.write("}")
        file.close()

    def whileStatemente(self, file, token, i, tab):
        file.write(((tab+1)*"\t") + "WhileStatement { \n")
        self.condition(file, token, i, tab)
        file.write(((tab+2)*"\t") + "},\n")
        file.write(((tab+2)*"\t") + "body: BlockStatement {\n")
        file.write(((tab+3)*"\t") + "body: [\n")

    def condition(self, file, token, i, tab):
        i = i+1
        print(self.tokens[i+1][0])
        if self.tokens[i+1][0] == '{NOT}':
            file.write(((tab+2)*"\t") + "condition:  UnaryExpression { \n")
            file.write(((tab+3)*"\t") + "operator: !\n")
            file.write(((tab+3)*"\t") + "argument: Identifier {\n")
            file.write(((tab+4)*"\t") + "name: "+ self.tokens[i+2][1] +"\n")
            file.write(((tab+3)*"\t") + "}\n")

        
        elif self.tokens[i+4][0] == '{)}':
            file.write(((tab+2)*"\t") + "condition:  BinaryExpression { \n")
            type_one, type_two = self.getType(self.tokens[i+1])
            file.write(((tab+3)*"\t") + "left: " + type_one + " {\n")
            file.write(((tab+4)*"\t") + type_two + ": " + self.tokens[i+1][1] +"\n")
            file.write(((tab+3)*"\t") + "}\n")
            file.write(((tab+3)*"\t") + "operator: " + self.tokens[i+2][1] + "\n")
            type_one, type_two = self.getType(self.tokens[i+3])
            file.write(((tab+3)*"\t") + "right: " + type_one + " {\n")
            file.write(((tab+4)*"\t") + type_two + ": " +  self.tokens[i+3][1] +"\n")
            file.write(((tab+3)*"\t") + "}\n")

        else:
            file.write(((tab+2)*"\t") + "condition:  LogicalExpression { \n")

            file.write(((tab+3)*"\t") + "left:  BinaryExpression { \n")
            type_one, type_two = self.getType(self.tokens[i+1])
            file.write(((tab+4)*"\t") + "left: " + type_one + " {\n")
            file.write(((tab+5)*"\t") + type_two + ": " +  self.tokens[i+1][1] +"\n")
            file.write(((tab+4)*"\t") + "}\n")
            file.write(((tab+4)*"\t") + "operator: " + self.tokens[i+2][1] + "\n")
            type_one, type_two = self.getType(self.tokens[i+3])
            file.write(((tab+4)*"\t") + "right: " + type_one + " {\n")
            file.write(((tab+5)*"\t") + type_two + ": " +  self.tokens[i+3][1] +"\n")
            file.write(((tab+4)*"\t") + "}\n")
            file.write(((tab+3)*"\t") + "}\n")
            
            file.write(((tab+3)*"\t") + "operator: " + self.tokens[i+4][1] + "\n")

            file.write(((tab+3)*"\t") + "right:  BinaryExpression { \n")
            type_one, type_two = self.getType(self.tokens[i+5])
            file.write(((tab+4)*"\t") + "left: " + type_one + " {\n")
            file.write(((tab+5)*"\t") + type_two + ": " +  self.tokens[i+5][1] +"\n")
            file.write(((tab+4)*"\t") + "}\n")
            file.write(((tab+4)*"\t") + "operator: " + self.tokens[i+6][1] + "\n")
            type_one, type_two = self.getType(self.tokens[i+7])
            file.write(((tab+4)*"\t") + "right: " + type_one + " {\n")
            file.write(((tab+5)*"\t") + type_two + ": " +  self.tokens[i+7][1] +"\n")
            file.write(((tab+4)*"\t") + "}\n")
            file.write(((tab+3)*"\t") + "}\n")





            

    def closeBody(self, file, token, i, tab):
        file.write(((tab+3)*"\t") + "]\n")
        file.write(((tab+2)*"\t") + "}\n")
        file.write(((tab+1)*"\t") + "}\n")


    def expressionStatement(self, file, token, i, tab):
        #verificar se é uma expressão simples a = b ou a = 1
        file.write(((tab+1)*"\t") + "ExpressionStatement { \n")
        file.write(((tab+2)*"\t") + "AssignmentExpression { \n")
        file.write(((tab+3)*"\t") + "operator : =\n")
    
        if self.tokens[i + 3][0] == "{;}" :
            file.write(((tab+3)*"\t") + "left : Indentifier {\n")
            file.write(((tab+4)*"\t") + "name : " + token[1] + '\n')
            file.write(((tab+3)*"\t") + "}, \n")
            type_one, type_two = self.getType(self.tokens[i+2])
            file.write(((tab+3)*"\t") + "right : "+ type_one +" {\n")
            file.write(((tab+4)*"\t") + type_two + " : " +  self.tokens[i+2][1] + '\n')
            file.write(((tab+3)*"\t") + "}, \n")
        else:
            file.write(((tab+3)*"\t") + "left : Indentifier {\n")
            file.write(((tab+4)*"\t") + "name : " + token[1] + '\n')
            file.write(((tab+3)*"\t") + "}, \n")
            
            file.write(((tab+3)*"\t") + "right : BinaryExpression { \n")
            
            type_one, type_two = self.getType(self.tokens[i+2])
            file.write(((tab+4)*"\t") + "left : "+ type_one +" {\n")
            file.write(((tab+5)*"\t") + type_two + " : " +  self.tokens[i+2][1] + '\n')
            file.write(((tab+4)*"\t") + "}, \n")

            file.write(((tab+4)*"\t") + "operator : "+ self.tokens[i+3][1] + "\n")

            
            type_one, type_two = self.getType(self.tokens[i+4])
            file.write(((tab+4)*"\t") + "right : "+ type_one +" {\n")
            file.write(((tab+5)*"\t") + type_two + " : " +  self.tokens[i+4][1] + '\n')
            file.write(((tab+4)*"\t") + "}, \n")

            file.write(((tab+3)*"\t") + "}\n")




        
        file.write(((tab+2)*"\t") + "}, \n")
        file.write(((tab+1)*"\t") + "}, \n")

    def getType(self, token):
        if token[0] == '{ID}':
            return "Identifier", "name"
        else:
            return "Literal", "value"

    def inputOutputDeclaration(self, file, token, id_token, tab):
        file.write(((tab+1)*"\t") + "InputOutputDeclaration { \n")
        file.write(((tab+2)*"\t") + "type: " + token[0][1:-1]+"\n")
        file.write(((tab+2)*"\t") + "id: " + id_token[1]+"\n")
        file.write(((tab+1)*"\t") + "}, \n")

    def variableDeclaration(self, file, token, next_token, tab):
        file.write(((tab+1)*"\t")+"VariableDeclaration { \n")
        file.write(((tab+2)*"\t")+"type: "+token[0][1:-1]+"\n")
        file.write(((tab+2)*"\t")+"name: "+next_token[1]+"\n")
        file.write(((tab+1)*"\t")+"}, \n")


#declarao variaveis int ->
#print -> ( ID )
#scan
#atribuicao de var   a = b   a = b + 1
            
#if -> child ( stmt )
#else - > { stmt }
#while -> child  ( stmt )