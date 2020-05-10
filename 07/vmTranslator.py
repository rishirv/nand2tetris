import sys

vmFile = sys.argv[1]
file = vmFile[vmFile.rfind('/')+1:vmFile.rfind('.')]
asmFile = vmFile[:vmFile.rfind('.')]+'.asm'

pullRAM = '@{{i}}\nD=A\n@{seg}\nA=D+M\nD=M\n'
pushStack = '@SP\nM=M+1\nA=M-1\nM=D\n' 
pushDict = {
    'constant': '@{i}\nD=A\n',
    'local':  pullRAM.format(seg='LCL'),
    'argument': pullRAM.format(seg='ARG'),
    'this': pullRAM.format(seg='THIS'),
    'that': pullRAM.format(seg='THAT'),
    'static': '@{file}.{{i}}\nD=M\n'.format(file=file),
    'temp': '@5\nD=A\n@{i}\nA=D+A\nD=M\n',
    'pointer': '@THIS\nD=A\n@{i}\nA=D+A\nD=M\n'
}

pullAddr = '@{{i}}\nD=A\n@{seg}\nD=D+M\n'
popStack = '@SP\nM=M-1\nA=M\nD=M\n@addr\nA=M\nM=D\n'
popDict = {
    'local':  pullAddr.format(seg='LCL'),
    'argument': pullAddr.format(seg='ARG'),
    'this': pullAddr.format(seg='THIS'),
    'that': pullAddr.format(seg='THAT'),
    'static': '@{file}.{{i}}\nD=A\n'.format(file=file),
    'temp': '@5\nD=A\n@{i}\nD=D+A\n',
    'pointer': '@THIS\nD=A\n@{i}\nD=D+A\n'
}

unary = '@SP\nA=M-1\nM={op}M\n'
binary = '@SP\nAM=M-1\nD=M\nA=A-1\nMD=M{op}D\n'
jump = 'M=-1\n@JUMP${{label}}\nD; {j}\n@SP\nA=M-1\nM=0\n(JUMP${{label}})\n'
currJump = 0
arith = {
    'neg': unary.format(op='-'),
    'not': unary.format(op='!'),
    'add': binary.format(op='+'),
    'sub': binary.format(op='-'),
    'and': binary.format(op='&'),
    'or': binary.format(op='|'),
    'eq': binary.format(op='-') + jump.format(j='JEQ'),
    'gt': binary.format(op='-') + jump.format(j='JGT'),
    'lt': binary.format(op='-') + jump.format(j='JLT')
}

f = open(asmFile, "w")
with open(vmFile, "r") as lines:
    for line in lines:
        comm = line.find('//') 
        line = line[:(len(line) if comm==-1 else comm)] #Remove comments
        l = line.split()
        if not l: #Comment or empty line
            continue
        elif len(l) == 1:
            f.write(arith[l[0]].format(label=currJump))
            currJump += 1
        elif len(l) == 3:
            if l[0] == 'push':
                f.write(pushDict[l[1]].format(i=l[2]))
                f.write(pushStack)
            else:
                f.write(popDict[l[1]].format(i=l[2]) + '@addr\nM=D\n')
                f.write(popStack)
f.write('(INFINITE_LOOP)\n@INFINITE_LOOP\n0; JEQ\n')
f.close()