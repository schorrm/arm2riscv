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

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>Opcode</th>
      <th>Instruction</th>
      <th>Translation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>
```asm
add
```
</td>
      <td>
```asm
add	x0, x0, :lo12:atomic_counter
```
</td>
      <td>
```asm
add	x10, x10, %lo(atomic_counter)
```
</td>
    </tr>
    <tr>
      <th>1</th>
      <td>
```asm
adrp
```
</td>
      <td>
```asm
adrp	x0, .LC8
```
</td>
      <td>
```asm
lui	x10, %hi(.LC8)
```
</td>
    </tr>
    <tr>
      <th>2</th>
      <td>
```asm
asr
```
</td>
      <td>
```asm
asr	w0, w0, 1
```
</td>
      <td>
```asm
sraiw	x10, x10, 1
```
</td>
    </tr>
    <tr>
      <th>3</th>
      <td>
```asm
b
```
</td>
      <td>
```asm
b	.L9
```
</td>
      <td>
```asm
j	.L9
```
</td>
    </tr>
    <tr>
      <th>4</th>
      <td>
```asm
beq
```
</td>
      <td>
```asm
beq	.L14
```
</td>
      <td>
```asm
beq	x25, x0, .L14
```
</td>
    </tr>
    <tr>
      <th>5</th>
      <td>
```asm
bge
```
</td>
      <td>
```asm
bge	.L11
```
</td>
      <td>
```asm
bge	x25, x0, .L11
```
</td>
    </tr>
    <tr>
      <th>6</th>
      <td>
```asm
bgt
```
</td>
      <td>
```asm
bgt	.L7
```
</td>
      <td>
```asm
bgt	x25, x0, .L7
```
</td>
    </tr>
    <tr>
      <th>7</th>
      <td>
```asm
bhi
```
</td>
      <td>
```asm
bhi	.L9
```
</td>
      <td>
```asm
bgt	x25, x0, .L9
```
</td>
    </tr>
    <tr>
      <th>8</th>
      <td>
```asm
bl
```
</td>
      <td>
```asm
bl	printf
```
</td>
      <td>asm
call	printf
```
</td>
    </tr>
    <tr>
      <th>9</th>
      <td>
```asm
ble
```
</td>
      <td>
```asm
ble	.L16
```
</td>
      <td>
```asm
ble	x25, x0, .L16
```
</td>
    </tr>
    <tr>
      <th>10</th>
      <td>
```asm
blt
```
</td>
      <td>
```asm
blt	.L10
```
</td>
      <td>
```asm
blt	x25, x0, .L10
```
</td>
    </tr>
    <tr>
      <th>11</th>
      <td>
```asm
bne
```
</td>
      <td>
```asm
bne	.L7
```
</td>
      <td>
```asm
bne	x25, x0, .L7
```
</td>
    </tr>
    <tr>
      <th>12</th>
      <td>
```asm
bpl
```
</td>
      <td>
```asm
bpl	.L5
```
</td>
      <td>
```asm
bge	x25, x0, .L5
```
</td>
    </tr>
    <tr>
      <th>13</th>
      <td>
```asm
cmp
```
</td>
      <td>
```asm
cmp	w0, 999
```
</td>
      <td>
```asm
addi	x25, x10, -999
```
</td>
    </tr>
    <tr>
      <th>14</th>
      <td>
```asm
csel
```
</td>
      <td>
```asm
csel x0, x10, x11, LE
```
</td>
      <td>
```asm
add	s11, x6, x0
ble	x25, x0, 999999f
add	s11, x7, x0
999999:
add	x10, x0, s11
```
</td>
    </tr>
    <tr>
      <th>15</th>
      <td>
```asm
eor
```
</td>
      <td>
```asm
eor	x1, x3, x1
```
</td>
      <td>
```asm
xor	x11, x13, x11
```
</td>
    </tr>
    <tr>
      <th>16</th>
      <td>
```asm
fadd
```
</td>
      <td>
```asm
fadd	d0, d1, d0
```
</td>
      <td>
```asm
fadd.d	f10, f11, f10
```
</td>
    </tr>
    <tr>
      <th>17</th>
      <td>
```asm
fcmp
```
</td>
      <td>
```asm
fcmp	d1, d0
```
</td>
      <td>
```asm
flt.d	x25, f11, f10 # this is less than, RHS is bigger
slli	x25, x25, 63 # move it to the sign bit location
flt.d	s11, f10, f11 # if LHS is bigger
or	x25, x25, s11 # or the results together
```
</td>
    </tr>
    <tr>
      <th>18</th>
      <td>
```asm
fcmpe
```
</td>
      <td>
```asm
fcmpe	d1, d0
```
</td>
      <td>
```asm
flt.d	x25, f11, f10 # this is less than, RHS is bigger
slli	x25, x25, 63 # move it to the sign bit location
flt.d	s11, f10, f11 # if LHS is bigger
or	x25, x25, s11 # or the results together
```
</td>
    </tr>
    <tr>
      <th>19</th>
      <td>
```asm
fdiv
```
</td>
      <td>
```asm
fdiv	d0, d0, d1
```
</td>
      <td>
```asm
fdiv.d	f10, f10, f11
```
</td>
    </tr>
    <tr>
      <th>20</th>
      <td>
```asm
fmadd
```
</td>
      <td>
```asm
fmadd d0, d0, d1, d2
```
</td>
      <td>
```asm
fmadd.d	f10, f10, f11, f12
```
</td>
    </tr>
    <tr>
      <th>21</th>
      <td>
```asm
fmov
```
</td>
      <td>
```asm
fmov	d1, x1
```
</td>
      <td>
```asm
fmv.d.x	f11, x11
```
</td>
    </tr>
    <tr>
      <th>22</th>
      <td>
```asm
fmsub
```
</td>
      <td>
```asm
fmsub d0, d0, d1, d2
```
</td>
      <td>
```asm
fnmsub.d	f10, f10, f11, f12
```
</td>
    </tr>
    <tr>
      <th>23</th>
      <td>
```asm
fmul
```
</td>
      <td>
```asm
fmul	d0, d1, d0
```
</td>
      <td>
```asm
fmul.d	f10, f11, f10
```
</td>
    </tr>
    <tr>
      <th>24</th>
      <td>
```asm
fneg
```
</td>
      <td>
```asm
fneg d0, d0
```
</td>
      <td>
```asm
fneg.d	f10, f10
```
</td>
    </tr>
    <tr>
      <th>25</th>
      <td>
```asm
fnmadd
```
</td>
      <td>
```asm
fnmadd d0, d0, d1, d2
```
</td>
      <td>
```asm
fnmadd.d	f10, f10, f11, f12
```
</td>
    </tr>
    <tr>
      <th>26</th>
      <td>
```asm
fnmsub
```
</td>
      <td>
```asm
fnmsub d0, d0, d1, d2
```
</td>
      <td>
```asm
fmsub.d	f10, f10, f11, f12
```
</td>
    </tr>
    <tr>
      <th>27</th>
      <td>
```asm
fsqrt
```
</td>
      <td>
```asm
fsqrt d0, d0
```
</td>
      <td>
```asm
fsqrt.d	f10, f10
```
</td>
    </tr>
    <tr>
      <th>28</th>
      <td>
```asm
fsub
```
</td>
      <td>
```asm
fsub	d0, d1, d0
```
</td>
      <td>
```asm
fsub.d	f10, f11, f10
```
</td>
    </tr>
    <tr>
      <th>29</th>
      <td>
```asm
ldaddal
```
</td>
      <td>
```asm
ldaddal	w1, w1, [x0]
```
</td>
      <td>
```asm
amoadd.w.aqrl	x11, x11, (x10)
```
</td>
    </tr>
    <tr>
      <th>30</th>
      <td>
```asm
ldar
```
</td>
      <td>
```asm
ldar	w0, [x0]
```
</td>
      <td>
```asm
lw	x10, 0(x10)
fence	iorw,iorw # making implicit fence semantics explicit
```
</td>
    </tr>
    <tr>
      <th>31</th>
      <td>
```asm
ldclral
```
</td>
      <td>
```asm
ldclral	w2, w2, [x0]
```
</td>
      <td>
```asm
not	s11, x12
amoand.w.aqrl	x12, s11, (x10)
```
</td>
    </tr>
    <tr>
      <th>32</th>
      <td>
```asm
ldeoral
```
</td>
      <td>
```asm
ldeoral	w1, w2, [x0]
```
</td>
      <td>
```asm
amoxor.w.aqrl	x12, x11, (x10)
```
</td>
    </tr>
    <tr>
      <th>33</th>
      <td>
```asm
ldp
```
</td>
      <td>
```asm
ldp	x29, x30, [sp], 48
```
</td>
      <td>
```asm
ld	x8, 0(sp)
ld	ra, 8(sp)
addi	sp, sp, 48 # writeback
```
</td>
    </tr>
    <tr>
      <th>34</th>
      <td>
```asm
ldr
```
</td>
      <td>
```asm
ldr	d0, [x0]
```
</td>
      <td>
```asm
fld	f10, 0(x10)
```
</td>
    </tr>
    <tr>
      <th>35</th>
      <td>
```asm
ldrsh
```
</td>
      <td>
```asm
ldrsh	w0, [x1, x0]
```
</td>
      <td>
```asm
add	s10, x10, x11 # converting offset register to add
lh	x10, 0(s10)
```
</td>
    </tr>
    <tr>
      <th>36</th>
      <td>
```asm
ldrsw
```
</td>
      <td>
```asm
ldrsw	x0, [x29, 28]
```
</td>
      <td>
```asm
lw	x10, 28(x8)
```
</td>
    </tr>
    <tr>
      <th>37</th>
      <td>
```asm
ldsetal
```
</td>
      <td>
```asm
ldsetal	w1, w2, [x0]
```
</td>
      <td>
```asm
amoor.w.aqrl	x12, x11, (x10)
```
</td>
    </tr>
    <tr>
      <th>38</th>
      <td>
```asm
ldsmaxal
```
</td>
      <td>
```asm
ldsmaxal x1, x1, [x0]
```
</td>
      <td>
```asm
amomax.d.aqrl	x11, x11, (x10)
```
</td>
    </tr>
    <tr>
      <th>39</th>
      <td>
```asm
ldsminal
```
</td>
      <td>
```asm
ldsminal x1, x1, [x0]
```
</td>
      <td>
```asm
amomin.d.aqrl	x11, x11, (x10)
```
</td>
    </tr>
    <tr>
      <th>40</th>
      <td>
```asm
ldumaxal
```
</td>
      <td>
```asm
ldumaxal x1, x1, [x0]
```
</td>
      <td>
```asm
amomaxu.d.aqrl	x11, x11, (x10)
```
</td>
    </tr>
    <tr>
      <th>41</th>
      <td>
```asm
lduminal
```
</td>
      <td>
```asm
lduminal x1, x1, [x0]
```
</td>
      <td>
```asm
amominu.d.aqrl	x11, x11, (x10)
```
</td>
    </tr>
    <tr>
      <th>42</th>
      <td>
```asm
lsl
```
</td>
      <td>
```asm
lsl	x0, x0, 2
```
</td>
      <td>
```asm
slli	x10, x10, 2
```
</td>
    </tr>
    <tr>
      <th>43</th>
      <td>
```asm
lsr
```
</td>
      <td>
```asm
lsr	w1, w0, 31
```
</td>
      <td>
```asm
srliw	x11, x10, 31
```
</td>
    </tr>
    <tr>
      <th>44</th>
      <td>
```asm
mov
```
</td>
      <td>
```asm
mov	x3, x0
```
</td>
      <td>
```asm
mv	x13, x10
```
</td>
    </tr>
    <tr>
      <th>45</th>
      <td>
```asm
movk
```
</td>
      <td>
```asm
movk	x0, 0x41df, lsl 48
```
</td>
      <td>
```asm
not	s11, x0 # set reg to all ones
srli	s11, s11, 48 # this clears the upper 48 bits in the mask. We'll invert it to get the final mask
li	s10, 16863 # load our immediate value
slli	s10, s10, 48 # move the immediate to the parallel place
slli	s11, s11, 48 # move the mask to the parallel place
not	s11, s11 # flip the mask to AND against
and	x10, x10, s11 # clear the target bits in mask
or	x10, x10, s10 # or in the bits from the immediate to load
```
</td>
    </tr>
    <tr>
      <th>46</th>
      <td>
```asm
mul
```
</td>
      <td>
```asm
mul	x1, x2, x1
```
</td>
      <td>
```asm
mul	x11, x12, x11
```
</td>
    </tr>
    <tr>
      <th>47</th>
      <td>
```asm
mvn
```
</td>
      <td>
```asm
mvn	w2, w2
```
</td>
      <td>
```asm
mv	x12, x12
not	x12, x12
```
</td>
    </tr>
    <tr>
      <th>48</th>
      <td>
```asm
neg
```
</td>
      <td>
```asm
neg	w0, w0
```
</td>
      <td>
```asm
sub	x10, x0, x10
```
</td>
    </tr>
    <tr>
      <th>49</th>
      <td>
```asm
nop
```
</td>
      <td>
```asm
nop
```
</td>
      <td>
```asm
nop
```
</td>
    </tr>
    <tr>
      <th>50</th>
      <td>
```asm
orr
```
</td>
      <td>
```asm
orr	x9, x1, x9
```
</td>
      <td>
```asm
or	x5, x11, x5
```
</td>
    </tr>
    <tr>
      <th>51</th>
      <td>
```asm
ret
```
</td>
      <td>
```asm
ret
```
</td>
      <td>
```asm
ret
```
</td>
    </tr>
    <tr>
      <th>52</th>
      <td>
```asm
scvtf
```
</td>
      <td>
```asm
scvtf	d0, w0
```
</td>
      <td>
```asm
fcvt.d.w	f10, x10
```
</td>
    </tr>
    <tr>
      <th>53</th>
      <td>
```asm
sdiv
```
</td>
      <td>
```asm
sdiv	w1, w1, w0
```
</td>
      <td>
```asm
divw	x11, x11, x10
```
</td>
    </tr>
    <tr>
      <th>54</th>
      <td>
```asm
stlr
```
</td>
      <td>
```asm
stlr	w1, [x0]
```
</td>
      <td>
```asm
fence	iorw,iorw  # making implicit fence semantics explicit
sw	x11, 0(x10)
```
</td>
    </tr>
    <tr>
      <th>55</th>
      <td>
```asm
stp
```
</td>
      <td>
```asm
stp	x29, x30, [sp, -64]!
```
</td>
      <td>
```asm
sd	x8, -64(sp)
sd	ra, -56(sp)
addi	sp, sp, -64 # writeback
```
</td>
    </tr>
    <tr>
      <th>56</th>
      <td>
```asm
str
```
</td>
      <td>
```asm
str	wzr, [x29, 76]
```
</td>
      <td>
```asm
sw	x0, 76(x8)
```
</td>
    </tr>
    <tr>
      <th>57</th>
      <td>
```asm
strh
```
</td>
      <td>
```asm
strh	w2, [x1, x0]
```
</td>
      <td>
```asm
add	s10, x10, x11 # converting offset register to add
sh	x12, 0(s10)
```
</td>
    </tr>
    <tr>
      <th>58</th>
      <td>
```asm
sub
```
</td>
      <td>
```asm
sub	w1, w0, w1
```
</td>
      <td>
```asm
subw	x11, x10, x11
```
</td>
    </tr>
    <tr>
      <th>59</th>
      <td>
```asm
sxtw
```
</td>
      <td>
```asm
sxtw	x1, w0
```
</td>
      <td>
```asm
sext.w	x11, x10
```
</td>
    </tr>
    <tr>
      <th>60</th>
      <td>
```asm
udiv
```
</td>
      <td>
```asm
udiv	w2, w0, w1
```
</td>
      <td>
```asm
divuw	x12, x10, x11
```
</td>
    </tr>
  </tbody>
</table>
