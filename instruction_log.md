|----|------------|-------------------------|-----------|
|  0 | `add`      | `add	x0, x0, :lo12:ts`                         | ```add	x10, x10, %lo(ts)```           |
|  1 | `adrp`     | `adrp	x0, .LC12`                         | ```lui	x10, %hi(.LC12)```           |
|  2 | `asr`      | `asr	w0, w0, 1`                         | ```sraiw	x10, x10, 1```           |
|  3 | `b`        | `b	.L11`                         | ```j	.L11```           |
|  4 | `beq`      | `beq	.L11`                         | ```beq	x25, x0, .L11```           |
|  5 | `bge`      | `bge	.L18`                         | ```bge	x25, x0, .L18```           |
|  6 | `bgt`      | `bgt	.L7`                         | ```bgt	x25, x0, .L7```           |
|  7 | `bl`       | `bl	printArray`                         | ```call	printArray```           |
|  8 | `ble`      | `ble	.L3`                         | ```ble	x25, x0, .L3```           |
|  9 | `blt`      | `blt	.L12`                         | ```blt	x25, x0, .L12```           |
| 10 | `bne`      | `bne	.L7`                         | ```bne	x25, x0, .L7```           |
| 11 | `cmp`      | `cmp	x0, 0`                         | ```addi	x25, x10, 0```           |
| 12 | `csel`     | `csel x0, x10, x11, LE` | ```add	s11, x6, x0
ble	x25, x0, 999999f
add	s11, x7, x0
999999:
add	x10, x0, s11```           |
| 13 | `eor`      | `eor	x0, x1, x0`                         | ```xor	x10, x11, x10```           |
| 14 | `fadd`     | `fadd	d0, d1, d0`                         | ```fadd.d	f10, f11, f10```           |
| 15 | `fdiv`     | `fdiv	d0, d1, d0`                         | ```fdiv.d	f10, f11, f10```           |
| 16 | `fmadd`    | `fmadd d0, d0, d1, d2`  | ```fmadd.d	f10, f10, f11, f12```           |
| 17 | `fmov`     | `fmov	d0, x0`                         | ```fmv.d.x	f10, x10```           |
| 18 | `fmsub`    | `fmsub d0, d0, d1, d2`  | ```fnmsub.d	f10, f10, f11, f12```           |
| 19 | `fmul`     | `fmul	d0, d1, d0`                         | ```fmul.d	f10, f11, f10```           |
| 20 | `fneg`     | `fneg d0, d0`           | ```fneg.d	f10, f10```           |
| 21 | `fnmadd`   | `fnmadd d0, d0, d1, d2` | ```fnmadd.d	f10, f10, f11, f12```           |
| 22 | `fnmsub`   | `fnmsub d0, d0, d1, d2` | ```fmsub.d	f10, f10, f11, f12```           |
| 23 | `fsqrt`    | `fsqrt d0, d0`          | ```fsqrt.d	f10, f10```           |
| 24 | `fsub`     | `fsub	d0, d1, d0`                         | ```fsub.d	f10, f11, f10```           |
| 25 | `ldaddal`  | `ldaddal	w1, w1, [x0]`                         | ```amoadd.w.aqrl	x11, x11, (x10)```           |
| 26 | `ldar`     | `ldar	w0, [x0]`                         | ```lw	x10, 0(x10)
fence	iorw,iorw # making implicit fence semantics explicit```           |
| 27 | `ldclral`  | `ldclral	w2, w2, [x0]`                         | ```not	s11, x12
amoand.w.aqrl	x12, s11, (x10)```           |
| 28 | `ldeoral`  | `ldeoral	w1, w2, [x0]`                         | ```amoxor.w.aqrl	x12, x11, (x10)```           |
| 29 | `ldp`      | `ldp	x29, x30, [sp]`                         | ```ld	x8, 0(x2)
ld	x1, 8(x2)```           |
| 30 | `ldr`      | `ldr	x3, [x2, 7256]`                         | ```li	s10, 7256 # synthesis of oversized offset
add	s10, x26, x12 # dealt with reg offset
ld	x13, 0(s10)```           |
| 31 | `ldrsh`    | `ldrsh	w0, [x1, x0]`                         | ```add	s10, x10, x11 # dealt with reg offset
lh	x10, 0(s10)```           |
| 32 | `ldrsw`    | `ldrsw	x1, [x29, 76]`                         | ```lw	x11, 76(x8)```           |
| 33 | `ldsetal`  | `ldsetal	w1, w2, [x0]`                         | ```amoor.w.aqrl	x12, x11, (x10)```           |
| 34 | `ldsmaxal` | `ldsmaxal x1, x1, [x0]` | ```amomax.d.aqrl	x11, x11, (x10)```           |
| 35 | `ldsminal` | `ldsminal x1, x1, [x0]` | ```amomin.d.aqrl	x11, x11, (x10)```           |
| 36 | `ldumaxal` | `ldumaxal x1, x1, [x0]` | ```amomaxu.d.aqrl	x11, x11, (x10)```           |
| 37 | `lduminal` | `lduminal x1, x1, [x0]` | ```amominu.d.aqrl	x11, x11, (x10)```           |
| 38 | `lsl`      | `lsl	x0, x0, 1`                         | ```slli	x10, x10, 1```           |
| 39 | `lsr`      | `lsr	x0, x0, 2`                         | ```srli	x10, x10, 2```           |
| 40 | `mov`      | `mov	x1,0`                         | ```li	x11, 0```           |
| 41 | `mul`      | `mul	w1, w1, w0`                         | ```mulw	x11, x11, x10```           |
| 42 | `mvn`      | `mvn	w2, w2`                         | ```mv	x12, x12
not	x12, x12```           |
| 43 | `neg`      | `neg	w0, w0`                         | ```sub	x10, x0, x10```           |
| 44 | `nop`      | `nop`                   | ```nop``` |
| 45 | `orr`      | `orr	x5, x1, x5`                         | ```or	x15, x11, x15```           |
| 46 | `ret`      | `ret`                   | ```ret``` |
| 47 | `sdiv`     | `sdiv	w2, w0, w1`                         | ```divw	x12, x10, x11```           |
| 48 | `stlr`     | `stlr	w1, [x0]`                         | ```fence	iorw,iorw  # making implicit fence semantics explicit
sw	x11, 0(x10)```           |
| 49 | `stp`      | `stp	x29, x30, [sp, -64]!`                         | ```sd	x8, -64(x2)
sd	x1, -56(x2)
addi	x2, x2, -64```           |
| 50 | `str`      | `str	w0, [x29, 84]`                         | ```sw	x10, 84(x8)```           |
| 51 | `strh`     | `strh	w2, [x1, x0]`                         | ```add	s10, x10, x11 # dealt with reg offset
sh	x12, 0(s10)```           |
| 52 | `sub`      | `sub	w1, w1, w0`                         | ```subw	x11, x11, x10```           |
| 53 | `sxtw`     | `sxtw	x1, w0`                         | ```sext.w	x11, x10```           |
| 54 | `udiv`     | `udiv	w2, w0, w1`                         | ```divuw	x12, x10, x11```           |