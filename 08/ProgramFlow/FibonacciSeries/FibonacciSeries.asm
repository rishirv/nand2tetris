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

@THIS
D=A
@1
D=D+A
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D
//pop pointer 1           
@0
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 0

@0
D=A
@THAT
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
//pop that 0              
@1
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 1

@1
D=A
@THAT
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
//pop that 1              
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

@2
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 2

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
(FibonacciSeries.MAIN_LOOP_START)
//label MAIN_LOOP_START

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
@FibonacciSeries.COMPUTE_ELEMENT
D; JNE
//if-goto COMPUTE_ELEMENT 
@FibonacciSeries.END_PROGRAM
0; JEQ
//goto END_PROGRAM        
(FibonacciSeries.COMPUTE_ELEMENT)
//label COMPUTE_ELEMENT

@0
D=A
@THAT
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
//push that 0

@1
D=A
@THAT
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
//push that 1

@SP
AM=M-1
D=M
A=A-1
MD=M+D
//add

@2
D=A
@THAT
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
//pop that 2              
@THIS
D=A
@1
A=D+A
D=M
@SP
M=M+1
A=M-1
M=D
//push pointer 1

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
MD=M+D
//add

@THIS
D=A
@1
D=D+A
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D
//pop pointer 1           
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
@FibonacciSeries.MAIN_LOOP_START
0; JEQ
//goto MAIN_LOOP_START

(FibonacciSeries.END_PROGRAM)
//label END_PROGRAM

