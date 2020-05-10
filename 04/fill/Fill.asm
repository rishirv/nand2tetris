// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

@color
M=0

(KEYLOOP)
@KBD
D=M
@WHITE
D; JEQ

@nextcol
M=-1
@CHANGE
0; JEQ

(WHITE)
@nextcol
M=0

(CHANGE)
@color
D=M
@nextcol
D=D-M
@KEYLOOP
D; JEQ

@color
M=!M

@SCREEN
D=A
@addr
M=D

(SETLOOP)
@addr
D=M
@KBD
D=D-A
@KEYLOOP
D; JEQ

@color
D=M
@addr
A=M
M=D
@addr
M=M+1

@SETLOOP
0; JEQ