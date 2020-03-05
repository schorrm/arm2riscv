# arm2riscv: An Arm to RISC-V Transpiler

Moshe Schorr and Matan Ivgi

Supervised by Hillel Mendelson, Shay Aviv, Hernan Theiler, and Tom Kolan
at IBM Labs Israel

Done as a one semester undergraduate project at the Technion VLSI Lab

## Background

RISC-V is a new and exciting open-source ISA. Open-sourcing the
processor architecture promises to simplify supply chains and
integration, as manufacturers could have all their subcomponents use the
same ISA, and avoid the complex IP issues that current ISAs suffer from.

The problem is that RISC-V is new, and there aren't many resources
available for it.

A *transpiler* is a tool that translates code between different
languages with an equivalent level of abstraction (in our case: assembly
to assembly), as a opposed to a compiler, which translates code from a
higher level of abstraction to a lower one.

Transpiling can allow, in some cases, direct porting of existing legacy
code, such as verification tools, firmware, and drivers to RISC-V, and
at the very least, greatly speed up the process of porting legacy code
to a new architecture.

**In this project we introduce an Arm to RISC-V transpiler.**

### Goals and Definitions

The goal for this project was to create a transpiler that can convert
convert moderately complex assembly code from Arm to RISC-V.

- 'Arm' here is defined as Arm's AArch64 ISA, including the atomic
instructions from Arm v8.3-a.

- 'RISC-V' here is defined as RISC-V 64G (=IMAFD). Where possible, we
aimed to cover as many instructions as possible in the target ISA.

## Possible Solutions

1. Direct transpilation of Arm assembly to RISC-V assembly.

2. Building a lifter from Arm assembly into LLVM IR (and then using
the LLVM toolchain to compile to the RISC-V target). This solution has
some advantages over direct transpilation, but suffers from some problems as
well, among them:

- Less consistency with the original code.
- Requires CFG construction and very complex deduction of the original logic.
- Deduction of original call.
- Dependencies include tools that are not yet mature.

Direct transpilation was selected.

## Difficulties

- Arm instructions can be very complicated to express with RISC-V instructions.
In many cases the equivalent code requires using other registers and calculations
that weren't "mentioned" originally in the Arm64 code.

- Arm's flexible second operand requires extensive modifications to accommodate.

- Handling the NCZV flags and a separated compare/branch model as opposed to the
fused compare-and-branch model used by RISC-V.

- Allocating registers:
    - In Arm there are 31 general purpose registers and an *additional* stack
    pointer, and in RISC-V there are 31 general purpose registers (SP included).
    We need to be able to allow logical use of all 32.
    - When adding various ABI restrictions (thread pointer, global pointer), the
    situation gets even worse.
    - Handling the extra complexity in Arm as described above requires even more
    registers for temporary usage.

- Different function calling conventions.

- Ensuring reliable and reproducible testing of the transpiler.

- Many minor details: different assembly format rules, etc....

The first three problems encouraged us to come up a general solution that
would treat this problems as one issue, namely, "the complex structure of
Arm assembly" (or, for that matter, "the simple structure of RISC-V
assembly").

Our solution for the resulting register stresss is to use thread local
storage as a pool of temp registers: we virtualize the use of some registers
to memory to get "more" registers and this frees up usable temp registers to
perform calculations for the translation and to emulate the flags.

## The Solution Architecture

The parser operates in three stages:

1. Convert the inputted assembly into a machine-readable representation.
This consists of several parts:
    1. Convert from text to a parsed, more machine-friendly form. We used
    [Lark](https://github.com/lark-parser/lark), a Python library that has
    a powerful and clean Lexer-Parser system. We defined (in our grammars
    folder) a formal grammar to parse Arm assembly, and then (in
    `convert_parse_tree.py`) a transformer to convert into simpler units
    for subsequent processing.
    2. Barrel shifted operands are removed from the operands list and
    promoted to separate instructions.
    3. Convert the parsed form into class objects that handle the logical
    translation of each individual instruction. This is handled by the
    class defined in `aarch64_instructions.py`, which are made available as
    subclasses of `Arm64Instruction`, allowing the parser to easily find
    which instructions we can parse and to delegate them accordingly.
        - Class objects report various details to the parser, for
        instance, which operands they modify, allowing the parser to
        handle the virtualized registers as needed.

2. Assign registers
    1. We mapping the names of registers (e.g. x0 --> x10) on the conversion
    classes.
    2. We receive from the conversion classes which virtualized registers they,
    modify, and then emit loads and stores accordingly.

3. We poll the classes to emit their corresponding RISC-V instructions.

### Register Mapping and Virtualization

We utilize 7 RISC-V registers for virtualization, temporaries, and emulating
language features:

1. X21 / S5 is the pointer to the "register bank" which is the memory we used for
the registers.

2. S6-8 / X22-24 are the registers used for holding registers from the virtualized
pool.

3. S9 / X25 is the register used for saving the compare results (a `cmp` instruction
is translated into a `sub` instruction that stores the result in S9).

4. S10 / X26 is used when a barrel shifted register is an operand.

5. S11 / X27 is used when general temp is required.

The bank is at the size of 8 doublewords (=64 bits), 1 for the extra register
in the Arm architecture and 7 more for the 7 registers mentioned above. When
invoking a instruction using an Arm register that was would by a straight mapping
of the calling convention be mapped to one of the above registers, or to a
register without a corresponding one in RISC-V, the X22, X23, or X24 registers are
used to hold them to operate on (since RISC-V does not allow direct operations
on memory). For example, `lsl   x10, x18, 5` becomes:

```asm
ld      x22, 8(x21) # load of mmapped register
slli    x6, x22, 5
```

## Arm Instructions Currently Supported

1. add
2. adrp
3. and
4. asr
5. b
6. beq
7. bge
8. bgt
9. bhi
10. bl
11. ble
12. blt
13. bne
14. bpl
15. cbnz
16. cmp
17. csel
18. cset
19. eor
20. fadd
21. fcmp
22. fcmpe
23. fdiv
24. fmadd
25. fmax
26. fmin
27. fmov
28. fmsub
29. fmul
30. fneg
31. fnmadd
32. fnmsub
33. fsqrt
34. fsub
35. ldadd
36. ldadda
37. ldaddal
38. ldaddl
39. ldar
40. ldaxr
41. ldclr
42. ldclra
43. ldclral
44. ldclrl
45. ldeor
46. ldeora
47. ldeoral
48. ldeorl
49. ldp
50. ldr
51. ldrb
52. ldrsh
53. ldrsw
54. ldset
55. ldseta
56. ldsetal
57. ldsetl
58. ldsmax
59. ldsmaxa
60. ldsmaxal
61. ldsmaxl
62. ldsmin
63. ldsmina
64. ldsminal
65. ldsminl
66. ldumax
67. ldumaxa
68. ldumaxal
69. ldumaxl
70. ldumin
71. ldumina
72. lduminal
73. lduminl
74. lsl
75. lsr
76. mov
77. movk
78. mul
79. mvn
80. neg
81. nop
82. orr
83. ret
84. scvtf
85. sdiv
86. stlr
87. stlxr
88. stp
89. str
90. strb
91. strh
92. sub
93. subs
94. swp
95. swpa
96. swpal
97. swpl
98. sxtw
99. ucvtf
100. udiv
101. umaddl

## Table of Examples

[See here](table.md)
