import sys
jumps = {'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT' : '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}
comps = {'0': '101010', '1': '111111', '-1': '111010', 'D': '001100', 'X': '110000', '!D': '001101', '!X': '110001', '-D': '001111', '-X': '110011', 'D+1': '011111', 'X+1':'110111', 'D-1': '001110', 'X-1': '110010', 'D+X': '000010', 'X+D': '000010', 'D-X': '010011', 'X-D': '000111', 'D&X': '000000', 'X&D': '000000', 'D|X': '010101', 'X|D': '010101'}
symbols = {'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15, 'SCREEN': 16384, 'KBD': '24576', 'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4}
asmFile = sys.argv[1]
hackFile = asmFile[:asmFile.rfind('.')]+'.hack'
f = open(hackFile, "w")
i = 0 #Line numbers
n = 16 #RAM address for variables
with open(asmFile, "r") as lines:
    for line in lines:
        l="".join(line.split()) #Remove whitespace
        comm = l.find('//') 
        l = l[:(len(l) if comm==-1 else comm)] #Remove comments
        if l and l[0] == '(' and l[-1] == ')': #Label Symbol
            symbols[l[1:-1]] = i
        elif l:
            i += 1
with open(asmFile, "r") as lines:
    for line in lines:
        l="".join(line.split()) #Remove whitespace
        comm = l.find('//') 
        l = l[:(len(l) if comm==-1 else comm)] #Remove comments
        if not l: #Comment or empty line
            pass
        elif l[0] == '(' and l[-1] == ')': #Label Symbol
            pass
        elif l[0] == '@': #A-Instruction
            try:
                num = int(l[1:]) #Integer instruction
            except:
                if l[1:] not in symbols: #Variable Symbol
                    symbols[l[1:]] = n #Add to list of variable
                    n += 1 #Increment RAM address
                num = symbols[l[1:]] #Variable symbol or label symbol
            f.write("0{n:015b}\n".format(n=num)) #0 followed by num in binary with up to 15 leading 0's
        else: #C-Instruction
            dest = jump = '000'
            equal = l.find('=')
            if equal>=0:
                d = l[:equal] #Destination in instruction
                dest = "".join(['1' if ch in d else '0' for ch in 'ADM']) #Dest bits
            semi = l.find(';')
            if semi>=0:
                j = l[semi+1:] #Jump in instruction
                jump = jumps[j] #Jump bits
            else:
                semi = len(l)
            c = l[equal+1:semi] #Computation in instruction
            a = '1' if 'M' in c else '0' #A bit
            comp = comps[c.replace('A', 'X').replace('M', 'X')] #Comp bits
            f.write("111{a}{comp}{dest}{jump}\n".format(a=a, comp=comp, dest=dest, jump=jump)) #111 followed by 1 A or M bit, 6 computation bits, 3 destination bits, and 3 jump bits
f.close()