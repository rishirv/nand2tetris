(SimpleFunction.test)
@SP
A=M
M=0
A=A+1
M=0
A=A+1
D=A
@SP
M=D
//function SimpleFunction.test 2

@0
D=A
@LCL
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
//push local 0

@1
D=A
@LCL
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
//push local 1

@SP
AM=M-1
D=M
A=A-1
MD=M+D
//add

@SP
A=M-1
M=!M
//not

@0
D=A
@ARG
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
//push argument 0

@SP
AM=M-1
D=M
A=A-1
MD=M+D
//add

@1
D=A
@ARG
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
//push argument 1

@SP
AM=M-1
D=M
A=A-1
MD=M-D
//sub

@LCL
D=M
@5
A=D-A
D=M
@ret
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@LCL
AM=M-1
D=M
@THAT
M=D
@LCL
AM=M-1
D=M
@THIS
M=D
@LCL
AM=M-1
D=M
@ARG
M=D
@LCL
AM=M-1
D=M
@LCL
M=D
@ret
A=M
0; JEQ
//return

