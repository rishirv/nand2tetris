@256
D=A
@SP
M=D
@$ret.0
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0; JEQ
($ret.0)
(Main.fibonacci)
@SP
A=M
D=A
@SP
M=D
//function Main.fibonacci 0

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
M=-1
@JUMP$0
D; JLT
@SP
A=M-1
M=0
(JUMP$0)
//lt                     
@SP
AM=M-1
D=M
@Main.vm.IF_TRUE
D; JNE
//if-goto IF_TRUE

@Main.vm.IF_FALSE
0; JEQ
//goto IF_FALSE

(Main.vm.IF_TRUE)
//label IF_TRUE          
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

(Main.vm.IF_FALSE)
//label IF_FALSE         
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

@Main.fibonacci$ret.0
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0; JEQ
(Main.fibonacci$ret.0)
//call Main.fibonacci 1  
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

@Main.fibonacci$ret.1
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0; JEQ
(Main.fibonacci$ret.1)
//call Main.fibonacci 1  
@SP
AM=M-1
D=M
A=A-1
MD=M+D
//add                    
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

(Sys.init)
@SP
A=M
D=A
@SP
M=D
//function Sys.init 0

@4
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 4

@Sys.init$ret.0
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0; JEQ
(Sys.init$ret.0)
//call Main.fibonacci 1   
(Sys.vm.WHILE)
//label WHILE

@Sys.vm.WHILE
0; JEQ
//goto WHILE              
