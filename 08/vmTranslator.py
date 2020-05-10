import sys, os

vm = sys.argv[1]
files = []
func = ''
directory = False
if(vm[-3:] == '.vm'):
    files = [(vm, vm[vm.rfind('/')+1:vm.rfind('.')])]
    asmFile = vm[:vm.rfind('.')]+'.asm'
else:
    directory = True
    for file in os.listdir(vm):
        if file.endswith('.vm'):
            files.append((vm + '/' + file, file))
    asmFile = vm + '/' + vm[vm.rfind('/')+1:]+'.asm'


pullRAM = '@{{i}}\nD=A\n@{seg}\nA=D+M\nD=M\n'
pushStack = '@SP\nM=M+1\nA=M-1\nM=D\n' 
pushDict = {
    'constant': '@{i}\nD=A\n',
    'local':  pullRAM.format(seg='LCL'),
    'argument': pullRAM.format(seg='ARG'),
    'this': pullRAM.format(seg='THIS'),
    'that': pullRAM.format(seg='THAT'),
    'static': '@{file}.{i}\nD=M\n',
    'temp': '@5\nD=A\n@{i}\nA=D+A\nD=M\n',
    'pointer': '@THIS\nD=A\n@{i}\nA=D+A\nD=M\n'
}

pullAddr = '@{{i}}\nD=A\n@{seg}\nD=D+M\n'
popStack = '@addr\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@addr\nA=M\nM=D\n'
popDict = {
    'local':  pullAddr.format(seg='LCL'),
    'argument': pullAddr.format(seg='ARG'),
    'this': pullAddr.format(seg='THIS'),
    'that': pullAddr.format(seg='THAT'),
    'static': '@{file}.{i}\nD=A\n',
    'temp': '@5\nD=A\n@{i}\nD=D+A\n',
    'pointer': '@THIS\nD=A\n@{i}\nD=D+A\n'
}

unary = '@SP\nA=M-1\nM={op}M\n'
binary = '@SP\nAM=M-1\nD=M\nA=A-1\nMD=M{op}D\n'
jump = 'M=-1\n@JUMP${{label}}\nD; {j}\n@SP\nA=M-1\nM=0\n(JUMP${{label}})\n'
currJump = 0
currCall = 0
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

branch = {
    'label': '({file}.{label})\n',
    'goto': '@{file}.{label}\n0; JEQ\n',
    'if-goto': '@SP\nAM=M-1\nD=M\n@{file}.{label}\nD; JNE\n'
}

f = open(asmFile, 'w')

def call(l):
    global currCall
    f.write('@{func}$ret.{currCall}\nD=A\n@SP\nM=M+1\nA=M-1\nM=D\n'.format(func=func, currCall=currCall))
    for i in ['LCL', 'ARG', 'THIS', 'THAT']:
        f.write('@{i}\nD=M\n@SP\nM=M+1\nA=M-1\nM=D\n'.format(i=i))
    f.write('@SP\nD=M\n@5\nD=D-A\n@{nArgs}\nD=D-A\n@ARG\nM=D\n'.format(nArgs=l[2]))
    f.write('@SP\nD=M\n@LCL\nM=D\n')
    f.write('@{func}\n0; JEQ\n'.format(func=l[1]))
    f.write('({func}$ret.{currCall})\n'.format(func=func, currCall=currCall))
    currCall += 1

if directory:
    f.write('@256\nD=A\n@SP\nM=D\n')
    call(['call', 'Sys.init', '0']) 

for vmFile, file in files:
    with open(vmFile, "r") as lines:
        for line in lines:
            comm = line.find('//') 
            line = line[:(len(line) if comm==-1 else comm)] #Remove comments
            l = line.split()
            if not l: #Comment or empty line
                continue
            elif len(l) == 1:
                if l[0] == 'return':
                    f.write('@LCL\nD=M\n@5\nA=D-A\nD=M\n@ret\nM=D\n')
                    f.write('@SP\nA=M-1\nD=M\n@ARG\nA=M\nM=D\n')
                    f.write('@ARG\nD=M\n@SP\nM=D+1\n')
                    for i in ['THAT', 'THIS', 'ARG', 'LCL']:
                        f.write('@LCL\nAM=M-1\nD=M\n@{i}\nM=D\n'.format(i=i))
                    f.write('@ret\nA=M\n0; JEQ\n')
                else:
                    f.write(arith[l[0]].format(label=currJump))
                    currJump += 1
            elif len(l) == 2:
                f.write(branch[l[0]].format(file=file, label=l[1]))
            elif len(l) == 3:
                if l[0] == 'push':
                    f.write(pushDict[l[1]].format(i=l[2], file=file))
                    f.write(pushStack)
                elif l[0] == 'pop':
                    f.write(popDict[l[1]].format(i=l[2], file=file))
                    f.write(popStack)
                elif l[0] == 'function':
                    func = l[1]
                    currCall = 0
                    f.write('({func})\n@SP\nA=M\n'.format(func=func))
                    for i in range(int(l[2])):
                        f.write('M=0\nA=A+1\n')
                    f.write('D=A\n@SP\nM=D\n')
                elif l[0] == 'call':
                    call(l)
f.close()