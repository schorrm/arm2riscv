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
to assembly), as opposed to a compiler, which translates code from a
higher level of abstraction to a lower one.

Transpiling can allow, in some cases, direct porting of existing legacy
code, such as verification tools, firmware, and drivers to RISC-V, and
at the very least, greatly speed up the process of porting legacy code
to a new architecture.

**In this project we introduce an Arm to RISC-V transpiler.**

### Goals and Definitions

The goal for this project was to create a transpiler that can
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

The first three problems encouraged us to come up with a general solution that
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
    1. We are mapping the names of registers (e.g. x0 --> x10) on the conversion
    classes.
    2. We receive from the conversion classes which virtualized registers they used,
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

4. S10 / X26 is used when a barrel shifted register (e.g. `x3 lsl 2`) is an operand.

5. S11 / X27 is used when a temporary is required (for example, when we need a mask in `movk`).

The bank is at the size of 8 doublewords (=64 bits), 1 for the extra register
in the Arm architecture and 7 more for the 7 registers mentioned above. When
invoking an instruction using an Arm register that was would by a straight mapping
of the calling convention be mapped to one of the above registers, or to a
register without a corresponding one in RISC-V, the X22, X23, or X24 registers are
used to hold them to operate on (since RISC-V does not allow direct operations
on memory). For example, `lsl   x10, x18, 5` becomes:

```asm
ld      x22, 8(x21) # load of mmapped register
slli    x6, x22, 5
```

## The Final Product

### The Main Script - `arm2riscv.py`

For simplicity of use in a toolchain, we read from `stdin` and write to `stdout`.

Running with the help flag will result in the following output:

```
usage: arm2riscv.py [-h] [-annot] [-p] [-xnames] [-logfile LOGFILE] [-vi]

optional arguments:
  -h, --help            show this help message and exit
  -annot, --annot-source
                        show original lines as comments
  -p, --permissive      allow untranslated operations
  -xnames, --xnames     Use xnames instead of ABI names
  -logfile LOGFILE, --logfile LOGFILE
                        Log table of used instructions to file
  -vi, --view-instructions
                        List opcodes with defined conversions and exit
```

The `--permissive` flag was added for use cases where conversion may not strictly speaking be possible. For example, system mode conversion cannot really be done without effectively writing a hypervisor, and hence there's no real possibility to convert a read from `SP_EL2` to RISC-V. `--permissive` allows that, it just prints a `!!!!!` warning after, so someone can convert the bulk of their code and then manually replace what isn't simply replaceable.

### Testing and Debugging

Throughout the project, we tested constantly against our test suite ([`test_suite.py`](../test_suite.py)). Our testing methodology was relatively simple: we wrote tests in C that would elicit the relevant opcodes and functions that we were adding. Where this wasn't possible at a high level description, we used compiler intrinsics (used extensively in the thread tests) or inlined assembly (especially for fused floating-point operations). We wrote a test suite to automatically compile and transpile all of our reference code (found in `testing/code`). Each file is compiled to Arm and transpiled through _arm2riscv_ to RISC-V, and then the output (running through `qemu`) is checked to match. We found this method to be very workable as it was both simple and robust. We found that small errors at the assembly level tend to escalate extremely quickly, and a minor offset will tend to lead extremely quickly to a SEGFAULT or some other error.

When we had a failure, we typically debugged it through `qemu`. We would transpile to an assembly file, and place an `unimp` right after our error if it didn't immediately crash the program (`unimp` is valid GCC asm for trapping an unimplemented opcode error at runtime). We did this because this ensured that the relevant logging would always be at the very bottom of the file. By running `qemu -singlestep -d cpu,in_asm` it would log the assembly for every line as well as the resulting CPU state, and then we would go through it line by line to find where we had diverged from our ideal state.

All of our tests are unoptimized (`-O0` flag in GCC). This is intentional, as optimization could easily allow the compiler to propagate constants instead of going through the test benchmarks.

## Appendices

### Register Conversion

The following is a listing of our conversions. For the sake of brevity, w is omitted, but it follows x (e.g. if x6 --> x16, then w6 --> x16, and the width gets moved to the opcode level as RISC-V assembly dictates).
At the bottom, those are named things that we use to help store things to keep our logical model functional, as described above in 'Register Mapping and Virtualization'. Where there is a number instead of a register, that is the offset of the register in the memory bank.
`sp` and `ra` were used instead of `x2` and `x1` in all modes, for legibility purposes.

|    | Arm           | RISCV-ABI   | RISCV-NoABI   |
|---:|:--------------|:------------|:--------------|
|  0 | x0            | a0          | x10           |
|  1 | x1            | a1          | x11           |
|  2 | x2            | a2          | x12           |
|  3 | x3            | a3          | x13           |
|  4 | x4            | a4          | x14           |
|  5 | x5            | a5          | x15           |
|  6 | x6            | a6          | x16           |
|  7 | x7            | a7          | x17           |
|  8 | x8            | s1          | x9            |
|  9 | x9            | t0          | x5            |
| 10 | x10           | t1          | x6            |
| 11 | x11           | t2          | x7            |
| 12 | x12           | t3          | x28           |
| 13 | x13           | t4          | x29           |
| 14 | x14           | t5          | x30           |
| 15 | x15           | t6          | x31           |
| 16 | x16           | s11         | x27           |
| 17 | x17           | 0           | 0             |
| 18 | x18           | 8           | 8             |
| 19 | x19           | s2          | x18           |
| 20 | x20           | s3          | x19           |
| 21 | x21           | s4          | x20           |
| 22 | x22           | 16          | 16            |
| 23 | x23           | 24          | 24            |
| 24 | x24           | 32          | 32            |
| 25 | x25           | 40          | 40            |
| 26 | x26           | 48          | 48            |
| 27 | x27           | 56          | 56            |
| 28 | x28           | 64          | 64            |
| 29 | x29           | s0          | x8            |
| 30 | x30           | ra          | ra            |
| 31 | xzr           | x0          | x0            |
| 32 | sp            | sp          | sp            |
| 33 | pc            | pc          | pc            |
|    | Special Usages|             |               |
| 34 | temp          | s11         | x27           |
| 35 | shift_temp    | s10         | x26           |
| 36 | compare       | s9          | x25           |
| 37 | banked_temp_1 | s6          | x22           |
| 38 | banked_temp_2 | s7          | x23           |
| 39 | banked_temp_3 | s8          | x24           |
| 40 | bank_pointer  | s5          | x21           |

### Arm Instructions Currently Supported

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
