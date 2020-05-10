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
(Sys.init)
@SP
A=M
D=A
@SP
M=D
//function Sys.init 0

@4000
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 4000	
@THIS
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
//pop pointer 0

@5000
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 5000

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
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.main
0; JEQ
(Sys.init$ret.0)
//call Sys.main 0

@5
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
//pop temp 1

(Sys.vm.LOOP)
//label LOOP

@Sys.vm.LOOP
0; JEQ
//goto LOOP

(Sys.main)
@SP
A=M
M=0
A=A+1
M=0
A=A+1
M=0
A=A+1
M=0
A=A+1
M=0
A=A+1
D=A
@SP
M=D
//function Sys.main 5

@4001
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 4001

@THIS
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
//pop pointer 0

@5001
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 5001

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

@200
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 200

@1
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
//pop local 1

@40
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 40

@2
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
//pop local 2

@6
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 6

@3
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
//pop local 3

@123
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 123

@Sys.main$ret.0
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
@Sys.add12
0; JEQ
(Sys.main$ret.0)
//call Sys.add12 1

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

@2
D=A
@LCL
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
//push local 2

@3
D=A
@LCL
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
//push local 3

@4
D=A
@LCL
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
//push local 4

@SP
AM=M-1
D=M
A=A-1
MD=M+D
//add

@SP
AM=M-1
D=M
A=A-1
MD=M+D
//add

@SP
AM=M-1
D=M
A=A-1
MD=M+D
//add

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

(Sys.add12)
@SP
A=M
D=A
@SP
M=D
//function Sys.add12 0

@4002
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 4002

@THIS
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
//pop pointer 0

@5002
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 5002

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

@12
D=A
@SP
M=M+1
A=M-1
M=D
//push constant 12

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

