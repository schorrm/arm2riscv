	.file	"floats_punned.c"
        .section .tdata
REG_BANK:
        .dword 0
        .dword 0
        .dword 0
        .dword 0
        .dword 0
        .dword 0
        .dword 0
        .dword 0
	.text
	.section	.rodata
	.align	3
.LC3:
	.string	"Floating ops"
	.align	3
.LC4:
	.string	"Addition: %lu\n"
	.align	3
.LC5:
	.string	"Subtraction: %lu\n"
	.align	3
.LC6:
	.string	"Multiplication: %lu\n"
	.align	3
.LC7:
	.string	"Divistion: %lu\n"
	.align	3
.LC8:
	.string	"Multiply-Add: %lu\n"
	.align	3
.LC9:
	.string	"Multiply-Subtract: %lu\n"
	.align	3
.LC10:
	.string	"Negative Multiply-Subtract: %lu\n"
	.align	3
.LC11:
	.string	"Negative Multiply-Add: %lu\n"
	.align	3
.LC12:
	.string	"FNegate: %lu\n"
	.align	3
.LC13:
	.string	"Square Root: %lu \n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	la	x21, REG_BANK
	# stp	x29, x30, [sp, -48]!
	sd	x8, -48(sp)
	sd	ra, -40(sp)
	addi	sp, sp, -48 # writeback
	# add	x29, sp, 0
	addi	x8, sp, 0
	# adrp	x0, .LC0
	lui	x10, %hi(.LC0)
	# add	x0, x0, :lo12:.LC0
	add	x10, x10, %lo(.LC0)
	# ldr	d0, [x0]
	fld	f10, 0(x10)
	# str	d0, [x29, 16]
	fsd	f10, 16(x8)
	# adrp	x0, .LC1
	lui	x10, %hi(.LC1)
	# add	x0, x0, :lo12:.LC1
	add	x10, x10, %lo(.LC1)
	# ldr	d0, [x0]
	fld	f10, 0(x10)
	# str	d0, [x29, 24]
	fsd	f10, 24(x8)
	# adrp	x0, .LC2
	lui	x10, %hi(.LC2)
	# add	x0, x0, :lo12:.LC2
	add	x10, x10, %lo(.LC2)
	# ldr	d0, [x0]
	fld	f10, 0(x10)
	# str	d0, [x29, 32]
	fsd	f10, 32(x8)
	# adrp	x0, .LC3
	lui	x10, %hi(.LC3)
	# add	x0, x0, :lo12:.LC3
	add	x10, x10, %lo(.LC3)
	# bl	puts
	call	puts
	# ldr	d1, [x29, 16]
	fld	f11, 16(x8)
	# ldr	d0, [x29, 24]
	fld	f10, 24(x8)
	# fadd	d0, d1, d0
	fadd.d	f10, f11, f10
	# str	d0, [x29, 40]
	fsd	f10, 40(x8)
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# adrp	x0, .LC4
	lui	x10, %hi(.LC4)
	# add	x0, x0, :lo12:.LC4
	add	x10, x10, %lo(.LC4)
	# bl	printf
	call	printf
	# ldr	d1, [x29, 16]
	fld	f11, 16(x8)
	# ldr	d0, [x29, 24]
	fld	f10, 24(x8)
	# fsub	d0, d1, d0
	fsub.d	f10, f11, f10
	# str	d0, [x29, 40]
	fsd	f10, 40(x8)
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# adrp	x0, .LC5
	lui	x10, %hi(.LC5)
	# add	x0, x0, :lo12:.LC5
	add	x10, x10, %lo(.LC5)
	# bl	printf
	call	printf
	# ldr	d1, [x29, 16]
	fld	f11, 16(x8)
	# ldr	d0, [x29, 24]
	fld	f10, 24(x8)
	# fmul	d0, d1, d0
	fmul.d	f10, f11, f10
	# str	d0, [x29, 40]
	fsd	f10, 40(x8)
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# adrp	x0, .LC6
	lui	x10, %hi(.LC6)
	# add	x0, x0, :lo12:.LC6
	add	x10, x10, %lo(.LC6)
	# bl	printf
	call	printf
	# ldr	d1, [x29, 16]
	fld	f11, 16(x8)
	# ldr	d0, [x29, 24]
	fld	f10, 24(x8)
	# fdiv	d0, d1, d0
	fdiv.d	f10, f11, f10
	# str	d0, [x29, 40]
	fsd	f10, 40(x8)
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# adrp	x0, .LC7
	lui	x10, %hi(.LC7)
	# add	x0, x0, :lo12:.LC7
	add	x10, x10, %lo(.LC7)
	# bl	printf
	call	printf
	# ldr	x0, [x29, 16]
	ld	x10, 16(x8)
	# ldr	x1, [x29, 24]
	ld	x11, 24(x8)
	# ldr	x2, [x29, 32]
	ld	x12, 32(x8)
	# fmov	d0, x0
	fmv.d.x	f10, x10
	# fmov	d1, x1
	fmv.d.x	f11, x11
	# fmov	d2, x2
	fmv.d.x	f12, x12
#APP
	# fmadd d0, d0, d1, d2
	fmadd.d	f10, f10, f11, f12
#NO_APP
	# str	d0, [x29, 40]
	fsd	f10, 40(x8)
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# adrp	x0, .LC8
	lui	x10, %hi(.LC8)
	# add	x0, x0, :lo12:.LC8
	add	x10, x10, %lo(.LC8)
	# bl	printf
	call	printf
	# ldr	x0, [x29, 16]
	ld	x10, 16(x8)
	# ldr	x1, [x29, 24]
	ld	x11, 24(x8)
	# ldr	x2, [x29, 32]
	ld	x12, 32(x8)
	# fmov	d0, x0
	fmv.d.x	f10, x10
	# fmov	d1, x1
	fmv.d.x	f11, x11
	# fmov	d2, x2
	fmv.d.x	f12, x12
#APP
	# fmsub d0, d0, d1, d2
	fnmsub.d	f10, f10, f11, f12
#NO_APP
	# str	d0, [x29, 40]
	fsd	f10, 40(x8)
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# adrp	x0, .LC9
	lui	x10, %hi(.LC9)
	# add	x0, x0, :lo12:.LC9
	add	x10, x10, %lo(.LC9)
	# bl	printf
	call	printf
	# ldr	x0, [x29, 16]
	ld	x10, 16(x8)
	# ldr	x1, [x29, 24]
	ld	x11, 24(x8)
	# ldr	x2, [x29, 32]
	ld	x12, 32(x8)
	# fmov	d0, x0
	fmv.d.x	f10, x10
	# fmov	d1, x1
	fmv.d.x	f11, x11
	# fmov	d2, x2
	fmv.d.x	f12, x12
#APP
	# fnmsub d0, d0, d1, d2
	fmsub.d	f10, f10, f11, f12
#NO_APP
	# str	d0, [x29, 40]
	fsd	f10, 40(x8)
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# adrp	x0, .LC10
	lui	x10, %hi(.LC10)
	# add	x0, x0, :lo12:.LC10
	add	x10, x10, %lo(.LC10)
	# bl	printf
	call	printf
	# ldr	x0, [x29, 16]
	ld	x10, 16(x8)
	# ldr	x1, [x29, 24]
	ld	x11, 24(x8)
	# ldr	x2, [x29, 32]
	ld	x12, 32(x8)
	# fmov	d0, x0
	fmv.d.x	f10, x10
	# fmov	d1, x1
	fmv.d.x	f11, x11
	# fmov	d2, x2
	fmv.d.x	f12, x12
#APP
	# fnmadd d0, d0, d1, d2
	fnmadd.d	f10, f10, f11, f12
#NO_APP
	# str	d0, [x29, 40]
	fsd	f10, 40(x8)
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# adrp	x0, .LC11
	lui	x10, %hi(.LC11)
	# add	x0, x0, :lo12:.LC11
	add	x10, x10, %lo(.LC11)
	# bl	printf
	call	printf
	# ldr	x0, [x29, 16]
	ld	x10, 16(x8)
	# fmov	d0, x0
	fmv.d.x	f10, x10
#APP
	# fneg d0, d0
	fneg.d	f10, f10
#NO_APP
	# str	d0, [x29, 40]
	fsd	f10, 40(x8)
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# adrp	x0, .LC12
	lui	x10, %hi(.LC12)
	# add	x0, x0, :lo12:.LC12
	add	x10, x10, %lo(.LC12)
	# bl	printf
	call	printf
	# ldr	x0, [x29, 16]
	ld	x10, 16(x8)
	# fmov	d0, x0
	fmv.d.x	f10, x10
#APP
	# fsqrt d0, d0
	fsqrt.d	f10, f10
#NO_APP
	# str	d0, [x29, 40]
	fsd	f10, 40(x8)
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# adrp	x0, .LC13
	lui	x10, %hi(.LC13)
	# add	x0, x0, :lo12:.LC13
	add	x10, x10, %lo(.LC13)
	# bl	printf
	call	printf
	# mov	w0, 0
	li	x10, 0
	# ldp	x29, x30, [sp], 48
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	addi	sp, sp, 48 # writeback
	# ret
	ret
	.size	main, .-main
	.section	.rodata
	.align	3
.LC0:
	.word	3786389468
	.word	1086860557
	.align	3
.LC1:
	.word	1154487209
	.word	1083394040
	.align	3
.LC2:
	.word	2684622566
	.word	1085280571
	.text
	.ident	"GCC: (Ubuntu/Linaro 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
