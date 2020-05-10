import sys, os, re

jack = sys.argv[1]
files = [] #Create list of files
func = ''
directory = False
if(jack[-5:] == '.jack'): #Single file
    files = [(jack, jack[jack.rfind('/')+1:jack.rfind('.')])]
else: #Directory
    for file in os.listdir(jack):
        if file.endswith('.jack'): #Find all jack files
            files.append((jack + '/' + file, file))

reToken = r'\/\*\*|\/\*|\*\/|\d+|".*"|[a-zA-Z_][a-zA-Z0-9_]*|[\{\}\(\)\[\]\.\-\*\/&|<>=~,;+]' #Regex to identify tokens
keywordTokens = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
symbolTokens = '\{\}()[].,;+-*/&|<>=~'
commentTokens = ['/**', '/*']
ignore = False #Ignore because comment
tokens = [] #List of tokens in the form of tuples (token, type)
markup = '<{1}> {0} </{1}>\n' #Markup format

def writeToken(i): #Write a single token
    f.write(markup.format(*tokens[i]))

def writeTokens(i, x): #Write the next x tokens from position i
    for j in range(i, i+x):
        writeToken(j)
    return i+x

def compileClass(i = 0):
    f.write('<class>\n')
    i = writeTokens(i, 3) #class Main {
    while tokens[i][0] != '}':
        if tokens[i][0] in ['static', 'field']:
            i = compileVarDec(i, 'classVarDec') #Compile variable declaration statement
        elif tokens[i][0] in ['constructor', 'function', 'method']:
            i = compileSubroutineDec(i) #Compile a subroutine declaration
    i = writeTokens(i, 1) #}
    f.write('</class>\n') 

def compileSubroutineDec(i): #Constructor / function / method
    f.write('<subroutineDec>\n')
    i = writeTokens(i, 4) #function int Hi (
    i = compileParameterList(i)
    i = writeTokens(i, 1) #)
    f.write('<subroutineBody>\n')
    i = writeTokens(i, 1) #{
    while tokens[i][0] == 'var':
        i = compileVarDec(i, 'varDec')
    if tokens[i][0] != '}':
        i = compileStatements(i)
    i = writeTokens(i, 1) #}
    f.write('</subroutineBody>\n')
    f.write('</subroutineDec>\n')
    return i

def compileParameterList(i): #Paramaters to a function
    f.write('<parameterList>\n')
    # while tokens[i][0] != ')':
    if tokens[i][0] != ')':
        i = writeTokens(i, 2) #int i
    while tokens[i][0] == ',':
        i = writeTokens(i, 3) #, int j
    f.write('</parameterList>\n')
    return i

def compileVarDec(i, s): #Either class or local variable declaration
    f.write('<{}>\n'.format(s))
    i = writeTokens(i, 3) #var int i
    while tokens[i][0] != ';':
        i = writeTokens(i, 2) #, j
    i = writeTokens(i, 1) #;
    f.write('</{}>\n'.format(s))
    return i

def compileStatements(i): #Compile a group of statements
    f.write('<statements>\n')
    while tokens[i][0] != '}':
        if tokens[i][0] == 'let':
            f.write('<letStatement>\n')
            i = writeTokens(i, 2) #let i
            if tokens[i][0] == '[':
                i = writeTokens(i, 1) #[
                i = compileExpression(i)
                i = writeTokens(i, 1) #]
            i = writeTokens(i, 1) #=
            i = compileExpression(i)
            i = writeTokens(i, 1) #;
            f.write('</letStatement>\n')
        elif tokens[i][0] == 'if':
            f.write('<ifStatement>\n')
            i = writeTokens(i, 2) #if(
            i = compileExpression(i)
            i = writeTokens(i, 2) #){
            i = compileStatements(i)
            i = writeTokens(i, 1) #}
            if tokens[i][0] == 'else':
                i = writeTokens(i, 2) #else{
                i = compileStatements(i)
                i = writeTokens(i, 1) #}
            f.write('</ifStatement>\n')              
        elif tokens[i][0] == 'while':
            f.write('<whileStatement>\n')
            i = writeTokens(i, 2) #while(
            i = compileExpression(i)
            i = writeTokens(i, 2) #){
            i = compileStatements(i)
            i = writeTokens(i, 1) #}
            f.write('</whileStatement>\n')
        elif tokens[i][0] == 'do':
            f.write('<doStatement>\n')
            i = writeTokens(i, 1) #do
            i = compileSubroutineCall(i)
            i = writeTokens(i, 1) #;
            f.write('</doStatement>\n')
        elif tokens[i][0] == 'return':
            f.write('<returnStatement>\n')
            i = writeTokens(i, 1) #return
            if tokens[i][0] != ';':
                i = compileExpression(i)
            i = writeTokens(i, 1) #;
            f.write('</returnStatement>\n')
    f.write('</statements>\n')
    return i

def compileExpression(i): #Term (op term)*
    f.write('<expression>\n')
    i = compileTerm(i)
    while tokens[i][0] in ['+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '=']:
        i = writeTokens(i, 1) #Operator
        i = compileTerm(i)
    f.write('</expression>\n')
    return i

def compileTerm(i):
    f.write('<term>\n')
    if tokens[i][1] in ['integerConstant', 'stringConstant'] or tokens[i][0] in ['true', 'false', 'null', 'this']:
        i = writeTokens(i, 1) #Just write token
    elif tokens[i][0] == '(':
        i = writeTokens(i, 1) #(
        i = compileExpression(i)
        i = writeTokens(i, 1) #)
    elif tokens[i][0] in ['-', '~']:
        i = writeTokens(i, 1) #unaryOp
        i = compileTerm(i)
    else:
        if tokens[i+1][0] == '(' or tokens[i+1][0] == '.':
            i = compileSubroutineCall(i)
        elif tokens[i+1][0] == '[':
            i = writeTokens(i, 2) #var[
            i = compileExpression(i)
            i = writeTokens(i, 1) #]
        else:
            i = writeTokens(i, 1)
    f.write('</term>\n')
    return i

def compileSubroutineCall(i):
    i = writeTokens(i, 1) #foo
    if tokens[i][0] == '.':
        i = writeTokens(i, 2) #.bar
    i = writeTokens(i, 1) #(
    i = compileExpressionList(i)
    i = writeTokens(i, 1) #)
    return i

def compileExpressionList(i): #Comma separated list of expressions
    f.write('<expressionList>\n')
    if tokens[i][0] != ')':
        i = compileExpression(i)
        while tokens[i][0] == ',':
            i = writeTokens(i, 1) #,
            i = compileExpression(i)
    f.write('</expressionList>\n')
    return i

for jackFile, file in files: #Go through each file
    tokens = []
    f = open(jackFile[:-5] + 'T.xml', 'w')
    f.write('<tokens>\n')
    with open(jackFile, "r") as lines:
        for line in lines:
            comm = line.find('//')
            line = line[:(len(line) if comm==-1 else comm)] #Remove comments
            for token in re.findall(reToken, line):
                if token in commentTokens: #Start comment
                    ignore = True
                    continue
                elif token == '*/': #End comment
                    ignore = False
                    continue
                elif ignore: #In comment
                    continue
                elif token in keywordTokens: #Keyword
                    tag = 'keyword'
                elif token in symbolTokens: #Symbol
                    token = token.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') #&<> doesn't format correctly in xml
                    tag = 'symbol'
                elif token[-1] == '"' and token[0] == '"': #String Constant
                    tag = 'stringConstant'
                    token = token[1:-1] #Remove "xxx" quotes at beginning and end
                elif re.match(r'\d+', token): #Integer Constant
                    tag = 'integerConstant'
                else: #Identifier
                    tag = 'identifier'
                f.write(markup.format(token, tag))
                tokens.append((token, tag))
    f.write('</tokens>\n')
    f.close()

    f = open(jackFile[:-5] + '.xml', 'w')
    compileClass() #Each file must begin with a class
    f.close()