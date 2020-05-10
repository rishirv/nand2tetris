import sys, os, re
from collections import defaultdict

jack = sys.argv[1]
files = [] #Create list of files
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

className = ''
classVars = dict()
localVars = dict()
varNums = defaultdict(int)
types = {'var': 'local', 'field': 'this', 'static': 'static'}
# symbols = {'+': 'add', '-': 'sub', '*', '/', '&', '|', '<', '>', '='}

def compileClass(i = 0):
    global className, classVars, localVars, varNums
    #class Main {
    className = tokens[i+1]
    classVars = dict()
    varNums.clear()
    i += 3
    while tokens[i][0] in ['static', 'field']:
        i = compileVarDec(i) #Compile variable declaration statement
    while tokens[i][0] in ['constructor', 'function', 'method']:
        i = compileSubroutineDec(i) #Compile a subroutine declaration
    i += 1 #}

def compileSubroutineDec(i): #Constructor / function / method
    #function int Hi (...){
    global localVars, varNums
    localVars.clear()
    varNums['local'] = 0
    if tokens[i][0] == 'method':
        localVars['this'] = 'argument 0'
        varNums['local'] += 1
    j = compileParameterList(i+4) + 2
    while tokens[j][0] == 'var':
        j = compileVarDec(j)
    f.write('function ' + tokens[i+2][0] + ' ' + str(varNums['local']) + '\n')
    if tokens[i][0] == 'method':
        f.write('push argument 0\npop pointer 0\n')
    i = j
    if tokens[i][0] != '}':
        i = compileStatements(i)
    return i + 1 #}

def compileParameterList(i): #Paramaters to a function
    global varNums, localVars
    if tokens[i][0] != ')': #int i
        localVars[tokens[i+1][0]] = 'argument ' + str(varNums['argument'])
        varNums['argument'] += 1
        i += 2
    while tokens[i][0] == ',': #, int j
        localVars[tokens[i+2][0]] = 'argument ' + str(varNums['argument'])
        varNums['argument'] += 1
        i += 3
    return i

def compileVarDec(i): #Either class or local variable declaration
    global varNums
    #var int i
    if tokens[i][0] == 'var':
        varList = localVars
    elif tokens[i][0] in ['static', 'field']:
        varList = classVars
    varType = types[tokens[i][0]]
    varList[tokens[i+2][0]] = varType + ' ' + str(varNums[varType])
    varNums[varType] += 1
    i += 3
    while tokens[i][0] != ';': #, j
        varList[tokens[i+1][0]] = varType + ' ' + str(varNums[varType])
        varNums[varType] += 1
        i += 2
    i += 1 #;
    return i

def compileStatements(i): #Compile a group of statements
    while tokens[i][0] != '}':
        if tokens[i][0] == 'let':
            i += 2 #let i
            if tokens[i][0] == '[':
                i += 1 #[
                i = compileExpression(i)
                i += 1 #]
            i += (1) #=
            i = compileExpression(i)
            i += (1) #;
        elif tokens[i][0] == 'if':
            i += (2) #if(
            i = compileExpression(i)
            i += (2) #){
            i = compileStatements(i)
            i += (1) #}
            if tokens[i][0] == 'else':
                i += (2) #else{
                i = compileStatements(i)
                i += (1) #}
        elif tokens[i][0] == 'while':
            i += (2) #while(
            i = compileExpression(i)
            i += (2) #){
            i = compileStatements(i)
            i += (1) #}
        elif tokens[i][0] == 'do':
            i = compileSubroutineCall(i+1) #do foo()
            i += 1 #;
        elif tokens[i][0] == 'return':
            i += 1 #return
            if tokens[i][0] != ';':
                i = compileExpression(i)
            f.write('return\n')
            i += 1 #;
    return i

def compileExpression(i): #Term (op term)*
    i = compileTerm(i)
    while tokens[i][0] in ['+', '-', '*', '/', '&', '|', '<', '>', '=']:
        j = compileTerm(i+1)
        f.write(tokens[i][0] + '\n')
        i = j
    return i

def compileTerm(i):
    if tokens[i][1] == 'integerConstant':
        f.write('push constant ' + str(tokens[i][0]) + '\n')
        i += 1
    elif tokens[i][1] == 'stringConstant' or tokens[i][0] in ['true', 'false', 'null', 'this']:
        i += (1) #Just write token
    elif tokens[i][0] == '(':
        i = compileExpression(i+1) + 1 #(...)
    elif tokens[i][0] in ['-', '~']:
        j = compileTerm(i)
        f.write(tokens[i][0] + '\n')
        i = j
    else:
        if tokens[i+1][0] == '(' or tokens[i+1][0] == '.':
            i = compileSubroutineCall(i)
        elif tokens[i+1][0] == '[':
            i += (2) #var[
            i = compileExpression(i)
            i += (1) #]
        else:
            if tokens[i][0] in localVars:
                f.write('push ' + localVars[tokens[i][0]] + '\n')
            elif tokens[i][0] in classVars:
                f.write('push ' + classVars[tokens[i][0]] + '\n')
            i += 1
    return i   

def compileSubroutineCall(i):
    if tokens[i][0] in localVars:
        f.write('push ' + localVars[tokens[i][0]] + '\n')
    elif tokens[i][0] in classVars:
        f.write('push ' + classVars[tokens[i][0]] + '\n')
    func = tokens[i][0]
    i += 1 #foo
    if tokens[i][0] == '.': #.bar
        func += '.' + tokens[i+1][0]
        i += 2
    i += 1 #(
    i, nArgs = compileExpressionList(i)
    f.write('call ' + func + ' ' + str(nArgs) + '\n')
    i += 1 #)
    return i

def compileExpressionList(i): #Comma separated list of expressions
    nArgs = 0
    if tokens[i][0] != ')':
        i = compileExpression(i)
        nArgs += 1
        while tokens[i][0] == ',':
            i += 1 #,
            i = compileExpression(i)
            nArgs += 1
    return i, nArgs

for jackFile, file in files: #Go through each file
    tokens = []
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
                    tag = 'symbol'
                elif token[-1] == '"' and token[0] == '"': #String Constant
                    tag = 'stringConstant'
                    token = token[1:-1] #Remove "xxx" quotes at beginning and end
                elif re.match(r'\d+', token): #Integer Constant
                    tag = 'integerConstant'
                else: #Identifier
                    tag = 'identifier'
                tokens.append((token, tag))

    f = open(jackFile[:-5] + '.vm', 'w')
    compileClass() #Each file must begin with a class
    f.close()