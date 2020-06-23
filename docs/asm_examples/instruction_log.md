|----|------------|-------------------------|-----------|
|  0 | `add`      | `add	x0, x0, :lo12:atomic_counter`                         | ```add	x10, x10, %lo(atomic_counter)```           |
|  1 | `adrp`     | `adrp	x0, .LC8`                         | ```lui	x10, %hi(.LC8)```           |
|  2 | `asr`      | `asr	w0, w0, 1`                         | ```sraiw	x10, x10, 1```           |
|  3 | `b`        | `b	.L9`                         | ```j	.L9```           |
|  4 | `beq`      | `beq	.L14`                         | ```beq	x25, x0, .L14```           |
|  5 | `bge`      | `bge	.L11`                         | ```bge	x25, x0, .L11```           |
|  6 | `bgt`      | `bgt	.L7`                         | ```bgt	x25, x0, .L7```           |
|  7 | `bhi`      | `bhi	.L9`                         | ```bgt	x25, x0, .L9```           |
|  8 | `bl`       | `bl	printf`                         | ```call	printf```           |
|  9 | `ble`      | `ble	.L16`                         | ```ble	x25, x0, .L16```           |
| 10 | `blt`      | `blt	.L10`                         | ```blt	x25, x0, .L10```           |
| 11 | `bne`      | `bne	.L7`                         | ```bne	x25, x0, .L7```           |
| 12 | `bpl`      | `bpl	.L5`                         | ```bge	x25, x0, .L5```           |
| 13 | `cmp`      | `cmp	w0, 999`                         | ```addi	x25, x10, -999```           |
| 14 | `csel`     | `csel x0, x10, x11, LE` | ```add	s11, x6, x0
ble	x25, x0, 999999f
add	s11, x7, x0
999999:
add	x10, x0, s11```           |
| 15 | `eor`      | `eor	x1, x3, x1`                         | ```xor	x11, x13, x11```           |
| 16 | `fadd`     | `fadd	d0, d1, d0`                         | ```fadd.d	f10, f11, f10```           |
| 17 | `fcmp`     | `fcmp	d1, d0`                         | ```flt.d	x25, f11, f10 # this is less than, RHS is bigger
slli	x25, x25, 63 # move it to the sign bit location
flt.d	s11, f10, f11 # if LHS is bigger
or	x25, x25, s11 # or the results together```           |
| 18 | `fcmpe`    | `fcmpe	d1, d0`                         | ```flt.d	x25, f11, f10 # this is less than, RHS is bigger
slli	x25, x25, 63 # move it to the sign bit location
flt.d	s11, f10, f11 # if LHS is bigger
or	x25, x25, s11 # or the results together```           |
| 19 | `fdiv`     | `fdiv	d0, d0, d1`                         | ```fdiv.d	f10, f10, f11```           |
| 20 | `fmadd`    | `fmadd d0, d0, d1, d2`  | ```fmadd.d	f10, f10, f11, f12```           |
| 21 | `fmov`     | `fmov	d1, x1`                         | ```fmv.d.x	f11, x11```           |
| 22 | `fmsub`    | `fmsub d0, d0, d1, d2`  | ```fnmsub.d	f10, f10, f11, f12```           |
| 23 | `fmul`     | `fmul	d0, d1, d0`                         | ```fmul.d	f10, f11, f10```           |
| 24 | `fneg`     | `fneg d0, d0`           | ```fneg.d	f10, f10```           |
| 25 | `fnmadd`   | `fnmadd d0, d0, d1, d2` | ```fnmadd.d	f10, f10, f11, f12```           |
| 26 | `fnmsub`   | `fnmsub d0, d0, d1, d2` | ```fmsub.d	f10, f10, f11, f12```           |
| 27 | `fsqrt`    | `fsqrt d0, d0`          | ```fsqrt.d	f10, f10```           |
| 28 | `fsub`     | `fsub	d0, d1, d0`                         | ```fsub.d	f10, f11, f10```           |
| 29 | `ldaddal`  | `ldaddal	w1, w1, [x0]`                         | ```amoadd.w.aqrl	x11, x11, (x10)```           |
| 30 | `ldar`     | `ldar	w0, [x0]`                         | ```lw	x10, 0(x10)
fence	iorw,iorw # making implicit fence semantics explicit```           |
| 31 | `ldclral`  | `ldclral	w2, w2, [x0]`                         | ```not	s11, x12
amoand.w.aqrl	x12, s11, (x10)```           |
| 32 | `ldeoral`  | `ldeoral	w1, w2, [x0]`                         | ```amoxor.w.aqrl	x12, x11, (x10)```           |
| 33 | `ldp`      | `ldp	x29, x30, [sp], 48`                         | ```ld	x8, 0(sp)
ld	ra, 8(sp)
addi	sp, sp, 48 # writeback```           |
| 34 | `ldr`      | `ldr	d0, [x0]`                         | ```fld	f10, 0(x10)```           |
| 35 | `ldrsh`    | `ldrsh	w0, [x1, x0]`                         | ```add	s10, x10, x11 # converting offset register to add
lh	x10, 0(s10)```           |
| 36 | `ldrsw`    | `ldrsw	x0, [x29, 28]`                         | ```lw	x10, 28(x8)```           |
| 37 | `ldsetal`  | `ldsetal	w1, w2, [x0]`                         | ```amoor.w.aqrl	x12, x11, (x10)```           |
| 38 | `ldsmaxal` | `ldsmaxal x1, x1, [x0]` | ```amomax.d.aqrl	x11, x11, (x10)```           |
| 39 | `ldsminal` | `ldsminal x1, x1, [x0]` | ```amomin.d.aqrl	x11, x11, (x10)```           |
| 40 | `ldumaxal` | `ldumaxal x1, x1, [x0]` | ```amomaxu.d.aqrl	x11, x11, (x10)```           |
| 41 | `lduminal` | `lduminal x1, x1, [x0]` | ```amominu.d.aqrl	x11, x11, (x10)```           |
| 42 | `lsl`      | `lsl	x0, x0, 2`                         | ```slli	x10, x10, 2```           |
| 43 | `lsr`      | `lsr	w1, w0, 31`                         | ```srliw	x11, x10, 31```           |
| 44 | `mov`      | `mov	x3, x0`                         | ```mv	x13, x10```           |
| 45 | `movk`     | `movk	x0, 0x41df, lsl 48`                         | ```not	s11, x0 # set reg to all ones
srli	s11, s11, 48 # this clears the upper 48 bits in the mask. We'll invert it to get the final mask
li	s10, 16863 # load our immediate value
slli	s10, s10, 48 # move the immediate to the parallel place
slli	s11, s11, 48 # move the mask to the parallel place
not	s11, s11 # flip the mask to AND against
and	x10, x10, s11 # clear the target bits in mask
or	x10, x10, s10 # or in the bits from the immediate to load```           |
| 46 | `mul`      | `mul	x1, x2, x1`                         | ```mul	x11, x12, x11```           |
| 47 | `mvn`      | `mvn	w2, w2`                         | ```mv	x12, x12
not	x12, x12```           |
| 48 | `neg`      | `neg	w0, w0`                         | ```sub	x10, x0, x10```           |
| 49 | `nop`      | `nop`                   | ```nop``` |
| 50 | `orr`      | `orr	x9, x1, x9`                         | ```or	x5, x11, x5```           |
| 51 | `ret`      | `ret`                   | ```ret``` |
| 52 | `scvtf`    | `scvtf	d0, w0`                         | ```fcvt.d.w	f10, x10```           |
| 53 | `sdiv`     | `sdiv	w1, w1, w0`                         | ```divw	x11, x11, x10```           |
| 54 | `stlr`     | `stlr	w1, [x0]`                         | ```fence	iorw,iorw  # making implicit fence semantics explicit
sw	x11, 0(x10)```           |
| 55 | `stp`      | `stp	x29, x30, [sp, -64]!`                         | ```sd	x8, -64(sp)
sd	ra, -56(sp)
addi	sp, sp, -64 # writeback```           |
| 56 | `str`      | `str	wzr, [x29, 76]`                         | ```sw	x0, 76(x8)```           |
| 57 | `strh`     | `strh	w2, [x1, x0]`                         | ```add	s10, x10, x11 # converting offset register to add
sh	x12, 0(s10)```           |
| 58 | `sub`      | `sub	w1, w0, w1`                         | ```subw	x11, x10, x11```           |
| 59 | `sxtw`     | `sxtw	x1, w0`                         | ```sext.w	x11, x10```           |
| 60 | `udiv`     | `udiv	w2, w0, w1`                         | ```divuw	x12, x10, x11```           |