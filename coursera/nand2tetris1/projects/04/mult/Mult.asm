// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Initialize sum to be zero
    @sum
    M = 0;

(LOOP)
// Load counter
    @R0
    D = M;

// Check counter is zero
    @END
    D; JEQ

    @R1
    D = M;
    @sum
    M = M + D;

//  Decrement counter
    @R0
    M = M - 1;

    @LOOP
    0; JMP

(END)
// Save @sum to @R2
    @sum
    D = M;
    @R2
    M = D;

    @END
    0; JMP