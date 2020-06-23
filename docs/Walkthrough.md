# Walkthrough

To try and explain what we did, we'll follow some examples through the system, from ARM to the resulting RISC-V. We'll pick four examples, covering a pretty full range of what we do, and we'll explain each stage through these four registers. These are chosen both for feature use and also to show the easy and the hard parts alike.

## Our Instructions

1. `sub w1, w0, w1`
2. `stp x29, x30, [sp, -128]!`
3. `ldr w1, [x0, x1, lsl 2]`
4. `movk x0, 0x41df, lsl 48`

Let's begin by quickly explaining what our instructions do.

1. `sub w1, w0, w1`: This is the simplest example. In pseudocode, this is: `w1 := w0 - w1`. The only potential catch with an instruction like this is either immediate operands, or setting the flags.

2. `stp x29, x30, [sp, -128]!` - `stp` is 'store pair' in Arm. In the Arm calling convention, `x29` is the frame pointer, the pointer to the fixed base of our memory frame - while SP moves FP remains constant. That way many things may have a constantly changing address relative to the stack pointer, but they'll keep a constant offset from the frame pointer. `x30` is the link register ,the address which we will return to from the function. `[sp, -128]!` denotes an offset of 128 from the stack pointer, with writeback (we'll discuss this in length later).
   This is a common assembly idiom at the beginning of a function call, to push the link register and frame pointer to the stack. The called function will want to take its own frame pointer, so it'll back up the previous one, and it'll call functions, so it'll need to provided a return address in the link register. These will be restored right at the end of the function for the return, where the link register will be the address it will return to, and it'll give the frame pointer back to the caller the way it was beforehand. In pseudocode this instruction is something like:

```pseudocode
addr1 = sp - 128
addr2 = addr1 + 8 // the pair is stored contiguously
store fp in addr1
store lr in addr2
sp = addr1 // this is the writeback
```

3. `ldr w1, [x0, x1, lsl 2]` - `ldr` is load register. Here, the complexity lies in the offset. `x0` is the base of the address, to which `x1` is added, however,after having been shifted two to the left. This `lsl` idiom is useful for alignment. For instance, if I have a array of 32 bit integers, the twelth element in the array would be `array + (12 * 4)` = `array + (12 << 2)`.
   In pseudocode we could describe this as:

```pseudocode
offset = x1 << 2
addr = x0 + offset
load addr to w1
```

4. `movk x0, 0x41df, lsl 48` - the most complex of the bunch. `movk` is "move 16-bit immediate into register, **keeping other bits unchanged**." The `lsl 48` can be thought of as a shift or the bit index to set. We could explain this as:

```pseudocode
set bits 63 to 48 of x0 to 0x41df
```

## Step 1: Parsed Representation

Strings are annoying to manipulate. So we need to get a better understanding of our input than just the strings we got in. For this, we programmed a formal grammar and used [Lark](https://github.com/lark-parser/lark), a formal grammar parsing library written for Python. We're going to skip over the minutiae of the grammatical definition, and focus on our resulting output. We parse to a Python `dict`, and that's what we'll then use.

Let's start with example #1, `sub w1, w0, w1`. (We're showing the full resulting dict here for documentation, in the upcoming ones we will omit the unnecessary ones to the example.)

```python
{
'operation': {
    'opcode': 'sub',
    'operands': [{
        'register': 'w1',
        'half_width': True,
        'type': 'gp',
        'writeback': False
    }, {
        'register': 'w0',
        'half_width': True,
        'type': 'gp',
        'writeback': False
    }, {
        'register': 'w1',
        'half_width': True,
        'type': 'gp',
        'writeback': False
    }]
}
}
```

We encode `'operation'` -- there are directives, labels, and operations. Only operations go through the same translation process, directives and labels mostly just go out as they came in. And then we have our opcode, `sub`, and we have our operands. w1, w0, and w1. Looking at the first:

`'register': 'w1'`, this tells us that it is a register named `w1`.

`'half_width': True`, it's 32 bits, not the full 64.

`'type': 'gp'`, it's general purpose, not floating point.

`'writeback': False`, there's no writeback.

Now let's look at #2, `stp x29, x30, [sp, -128]!`. This going to be more complex (omitting the outer layer):

```python
{'opcode': 'stp',
'operands': [{
    'register': 'x29',
    'half_width': False,
    'type': 'gp',
    'writeback': False
}, {
    'register': 'x30',
    'half_width': False,
    'type': 'gp',
    'writeback': False
}, {
    'register': 'sp',
    'half_width': False,
    'type': 'gp',
    'indirect': True,
    'offset': -128,
    'writeback': True
}]}
```

`half_width` is false here since these are all 64-bit registers. Let's look at the last part of our parse tree here. This encodes the last operand here, `[sp, -128]!`. We add two things: it's an indirect access (`[]`), and there's an offset involved, `-128`. In addition, the `!` denotes writeback, which we then mark on the operand.

For #3, `ldr w1, [x0, x1, lsl 2]`, we have another complex case come up. Here we have a very busy second operand. Let's look the parse tree for just `[x0, x1, lsl 2]`.

```python
{
'register': 'x0',
'half_width': False,
'type': 'gp',
'indirect': True,
'offset': {
    'half_width': False,
    'register': 'shift_temp',
    'shift': {
        'shift_reg': {
            'register': 'x1',
            'half_width': False,
            'type': 'gp'
        },
        'shift_by': { 'immediate': 2 },
        'shift_type': 'lsl'
    },
    'type': 'gp'
},
'writeback': False
}
```

It's sort of like what we saw before in the `stp` case, except we now have a very complicated offset. We're going to mark this `shift_temp`, an abstraction we provide for shifted operands throughout the codebase. We do this since shifted operands in Arm aren't changed, they're retained as unshifted. So x1 is affected because it appears on the destination here, but if this were `ldr w2, [x0, x1, lsl 2]` x1 would be unchanged by the operation.
We then also encode the 'shift'. The register x1 is to be shifted, it is to be shifted by an immediate value of 2, and the shift type is `lsl`, 'logical shift left'.

## Stage 2: Pulling out shifts

RISC-V doesn't allow shifted operands. So we handle this after the initial parse. We look for shifted operands, and then wherever we find one we yank it out of the parse tree and make separate instruction for it, and put the result in its place. So our shift in `ldr w1, [x0, x1, lsl 2]` is going to be intercepted here and emitted as a separate shift operation, and then `ldr` will be using `shift_temp`, not doing the shift itself.

## Stage 3: Conversion Classes

Each instruction is handled by a class. This is going to called by the main script to handle the instructions that it declares itself able to handle. No instruction has more than one handler, some classes handle multiple instructions.All conversion classes inherit from a base class, `Arm64Instruction`, which provides several convenience methods.

Let's start with #1. this is the conversion class for subtract. We register at the top `opcodes`, a list of the opcodes which it can handle. In this case `sub`, as well as `subs`, which is 'subtract and set flags', setting the flags to the result of the subtract operation. We here define an `__init__` method, to be called on create (some classes don't need this, just superclassing Arm64Instruction), and an `emit_riscv` method, which creates the output line (this is mandatory).

```python
class Subtract(Arm64Instruction):
    """ Handle Subtract

    Along with updating flags if it's `subs`
    If possible, switches a sub with immediate to addi with flipped sign.
    """
    opcodes = ['sub', 'subs']

    def __init__(self, opcode, operands):
        super().__init__(opcode, operands)

        self.op = 'sub'
        if self.is_safe_imm(self.operands[2]):
            self.op = 'addi'
            self.immediate_value = -self.operands[2]['immediate']
        self.op += self.wflag
        if self.opcode == 'subs':
            self.specific_regs.append(COMPARE)

    def emit_riscv(self):
        super().emit_riscv()
        dest, s1, s2 = self.get_args()
        if self.immediate_value:
            s2 = self.immediate_value
        self.riscv_instructions += [
            f'{self.op} {dest}, {s1}, {s2}'
        ]
        if self.opcode == 'subs':
            cond = self.specific_regs[-1]
            self.riscv_instructions.append(
                f'mv {cond}, {dest} # simulating updating flags'
```

So there are two unusual things going on in the constructor. Let's take a closer look:

```python
if self.is_safe_imm(self.operands[2]):
    self.op = 'addi'
    self.immediate_value = -self.operands[2]['immediate']
```

What are we doing? Well, if the last operand is an immediate, and it's safe (= within the range that we can encode in a RISC-V operation, which is narrower than Arm), we want to work with it. However, RISC-V doesn't have a 'sub immediate' instruction, so we would instead put out an add immediate with a flipped operand.

We then see `self.op += self.wflag`. That's adding on a 'w' to the opcode if `wflag` is set, where `wflag` is provided by the class constructor to mark where the destination register is 32-bit. RISC-V supports 32 bit operations, but it marks them in the opcode, not in the register operand, so it'll be `subw` or `addiw`. And the next thing:

```python
if self.opcode == 'subs':
    self.specific_regs.append(COMPARE)
```

Here, we tell the global that we need to get the comparison register (the way we simulate the flags) if the opcode is `subs`. When we construct these classes, we don't have the RISC-V names in place. We work with logical registers, and then we swap in the precise information later. Let's look at one more constructor, the one for #4, movk. We're going to notify that we need temp and a shift_temp register, and we'll also look at some instruction-specific info.

```python
def __init__(self, opcode, operands):
    super().__init__(opcode, operands)
    self.required_temp_regs = ['temp', 'shift_temp']
    self.shift = False
    if len(self.operands) > 2:  # Not just a movk, but shifted
        self.shift = True
        # Operands are e.g. movk    x0, 0x41df, lsl 48
        # We never need to pull the shift, since it can only be LSL
        self.shamt = self.operands[3]['immediate']
```

Here, we have a unique factor to this instruction, the shift amount, which is going to be where this stored.

## Stage 4: Updating Registers

This is described in the main documentation, with a table of the conversions. We basically just plug in the parallel registers, and where necessary, we use loads and stores for things that were mapped to memory. We change the `specific_registers` and `required_temp_regs` to point to valid register names at this point. This is done from outside the classes on the class objects.

## Stage 5: Emits

The last stage here is the emits. We now have valid register names in the RISC-V ABI, so we have our assumptions corrected. Let's now go through our examples.

For #1, `sub w1, w0, w1`, we essentially just plug in the op which we calculated above, and then if we have the flags set, we copy our result to the simulated flags.

```python
def emit_riscv(self):
    super().emit_riscv()
    dest, s1, s2 = self.get_args()
    if self.immediate_value:
        s2 = self.immediate_value
    self.riscv_instructions += [
        f'{self.op} {dest}, {s1}, {s2}'
    ]
    if self.opcode == 'subs':
        cond = self.specific_regs[-1]
        self.riscv_instructions.append(
            f'mv {cond}, {dest} # simulating updating flags'
```

After emit, we would then get the following:

```asm
subw    x11, x10, x11
```

For `stp x29, x30, [sp, -128]!`, we have a very similar type of structure. RISC-V doesn't support writeback, so we tack in an add instruction if we have to. We put out a store instruction for both registers, and at the end update the stack pointer if we need writeback.

```python
def emit_riscv(self):
    r1, r2, sp = self.specific_regs
    self.riscv_instructions = [
        f'{self.base_op} {r1}, {self.offset}({sp})',
        f'{self.base_op} {r2}, {self.offset + 8}({sp})'
    ]

    if self.final_offset:
        self.riscv_instructions.append(
            f'addi {sp}, {sp}, {self.final_offset} # writeback'
```

After emit, we would then get:

```asm
sd      fp, -128(sp)
sd      ra, -120(sp)
addi    sp, sp, -128 # writeback
```

For #3, `ldr w1, [x0, x1, lsl 2]`, we would get the following (the `slli` on top having come from the `lsl` handler, not `ldr`):

```asm
slli    x26, x11, 2
add     x26, x26, x10 # converting offset register to add
lw      x11, 0(x26)
```

For #4, `movk x0, 0x41df, lsl 48`, we need a very complicated handler, and it'll handle a pretty complicated sequence here. We need to synthesize the complex logic, and the constant 0x41df is actually large enough to require its own `li`, load immediate, instruction in RISC-V:

```python
def emit_riscv(self):
    temp, shift_temp = self.required_temp_regs
    dest = self.specific_regs[0]
    imm = self.operands[1]['immediate']
    self.riscv_instructions = [
        f'not {temp}, x0 # set reg to all ones',
        f"srli {temp}, {temp}, 48 # this clears the upper 48 bits in the mask. We'll invert it to get the final mask",
        f"li {shift_temp}, {imm} # load our immediate value"
    ]
    if self.shift:
        self.riscv_instructions += [
            f'slli {shift_temp}, {shift_temp}, {self.shamt} # move the immediate to the parallel place',
            f'slli {temp}, {temp}, {self.shamt} # move the mask to the parallel place'
        ]
    self.riscv_instructions += [
        f'not {temp}, {temp} # flip the mask to AND against',
        f'and {dest}, {dest}, {temp} # clear the target bits in mask',
        f'or {dest}, {dest}, {shift_temp} # or in the bits from the immediate to load'
        ]
```

Resulting in the following assembly code:

```asm
not     x27, x0 # set reg to all ones
srli    x27, x27, 48 # this clears the upper 48 bits in the mask. We'll invert it to get the final mask
li      x26, 16863 # load our immediate value
slli    x26, x26, 48 # move the immediate to the parallel place
slli    x27, x27, 48 # move the mask to the parallel place
not     x27, x27 # flip the mask to AND against
and     x10, x10, x27 # clear the target bits in mask
or      x10, x10, x26 # or in the bits from the immediate to load
```

To rephrase this in pseudocode:

```pseudocode
mask = 0x0000ffffffffffff
imm  = 0x41df << 48
temp = x0 & mask // clear the parallel bits
x0   = imm | temp
```

This complexity is an unavoidable consequence of the more complex operations available in Arm64 (also, some extra instructions appear here for performance reasons.)
