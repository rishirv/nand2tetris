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
(Class1.set)
@SP
A=M
D=A
@SP
M=D
//function Class1.set 0

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

@Class1.vm.0
D=A
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D
//pop static 0

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

@Class1.vm.1
D=A
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D
//pop static 1

@0
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 0

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

(Class1.get)
@SP
A=M
D=A
@SP
M=D
//function Class1.get 0

@Class1.vm.0
D=M
@SP
M=M+1
A=M-1
M=D
//push static 0

@Class1.vm.1
D=M
@SP
M=M+1
A=M-1
M=D
//push static 1

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

(Class2.set)
@SP
A=M
D=A
@SP
M=D
//function Class2.set 0

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

@Class2.vm.0
D=A
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D
//pop static 0

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

@Class2.vm.1
D=A
@addr
M=D
@SP
M=M-1
A=M
D=M
@addr
A=M
M=D
//pop static 1

@0
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 0

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

(Class2.get)
@SP
A=M
D=A
@SP
M=D
//function Class2.get 0

@Class2.vm.0
D=M
@SP
M=M+1
A=M-1
M=D
//push static 0

@Class2.vm.1
D=M
@SP
M=M+1
A=M-1
M=D
//push static 1

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

(Sys.init)
@SP
A=M
D=A
@SP
M=D
//function Sys.init 0

@6
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 6

@8
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 8

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
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0; JEQ
(Sys.init$ret.0)
//call Class1.set 2

@5
D=A
@0
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
//pop temp 0 
@23
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 23

@15
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 15

@Sys.init$ret.1
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
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0; JEQ
(Sys.init$ret.1)
//call Class2.set 2

@5
D=A
@0
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
//pop temp 0 
@Sys.init$ret.2
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
@Class1.get
0; JEQ
(Sys.init$ret.2)
//call Class1.get 0

@Sys.init$ret.3
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
@Class2.get
0; JEQ
(Sys.init$ret.3)
//call Class2.get 0

(Sys.vm.WHILE)
//label WHILE

@Sys.vm.WHILE
0; JEQ
//goto WHILE

