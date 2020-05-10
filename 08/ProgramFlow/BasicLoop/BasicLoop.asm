@0
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 0    

@0
D=A
@LCL
D=D+M
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D
//pop local 0         
(BasicLoop.LOOP_START)
//label LOOP_START

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

@SP
AM=M-1
D=M
A=A-1
MD=M+D
//add

@0
D=A
@LCL
D=D+M
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D
//pop local 0	        
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

@1
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 1

@SP
AM=M-1
D=M
A=A-1
MD=M-D
//sub

@0
D=A
@ARG
D=D+M
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D
//pop argument 0      
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
@BasicLoop.LOOP_START
D; JNE
//if-goto LOOP_START  
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

