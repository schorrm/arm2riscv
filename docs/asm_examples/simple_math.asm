	.file	"simple_math.c"
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
.LC0:
	.string	"Signed Ops:"
	.align	3
.LC1:
	.string	"Addition: %d\n"
	.align	3
.LC2:
	.string	"Subtraction: %d\n"
	.align	3
.LC3:
	.string	"Multiplication: %d\n"
	.align	3
.LC4:
	.string	"Division: %d\n"
	.align	3
.LC5:
	.string	"Modulus: %d\n"
	.align	3
.LC6:
	.string	"Unsigned Ops:"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	la	x21, REG_BANK
	# stp	x29, x30, [sp, -32]!
	sd	x8, -32(sp)
	sd	ra, -24(sp)
	addi	sp, sp, -32 # writeback
	# add	x29, sp, 0
	addi	x8, sp, 0
	# mov	w0, 99
	li	x10, 99
	# str	w0, [x29, 16]
	sw	x10, 16(x8)
	# mov	w0, 10
	li	x10, 10
	# str	w0, [x29, 20]
	sw	x10, 20(x8)
	# adrp	x0, .LC0
	lui	x10, %hi(.LC0)
	# add	x0, x0, :lo12:.LC0
	add	x10, x10, %lo(.LC0)
	# bl	puts
	call	puts
	# ldr	w1, [x29, 16]
	lw	x11, 16(x8)
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# add	w1, w1, w0
	addw	x11, x11, x10
	# adrp	x0, .LC1
	lui	x10, %hi(.LC1)
	# add	x0, x0, :lo12:.LC1
	add	x10, x10, %lo(.LC1)
	# bl	printf
	call	printf
	# ldr	w1, [x29, 16]
	lw	x11, 16(x8)
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# sub	w1, w1, w0
	subw	x11, x11, x10
	# adrp	x0, .LC2
	lui	x10, %hi(.LC2)
	# add	x0, x0, :lo12:.LC2
	add	x10, x10, %lo(.LC2)
	# bl	printf
	call	printf
	# ldr	w1, [x29, 16]
	lw	x11, 16(x8)
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# mul	w1, w1, w0
	mulw	x11, x11, x10
	# adrp	x0, .LC3
	lui	x10, %hi(.LC3)
	# add	x0, x0, :lo12:.LC3
	add	x10, x10, %lo(.LC3)
	# bl	printf
	call	printf
	# ldr	w1, [x29, 16]
	lw	x11, 16(x8)
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# sdiv	w1, w1, w0
	divw	x11, x11, x10
	# adrp	x0, .LC4
	lui	x10, %hi(.LC4)
	# add	x0, x0, :lo12:.LC4
	add	x10, x10, %lo(.LC4)
	# bl	printf
	call	printf
	# ldr	w0, [x29, 16]
	lw	x10, 16(x8)
	# ldr	w1, [x29, 20]
	lw	x11, 20(x8)
	# sdiv	w2, w0, w1
	divw	x12, x10, x11
	# ldr	w1, [x29, 20]
	lw	x11, 20(x8)
	# mul	w1, w2, w1
	mulw	x11, x12, x11
	# sub	w1, w0, w1
	subw	x11, x10, x11
	# adrp	x0, .LC5
	lui	x10, %hi(.LC5)
	# add	x0, x0, :lo12:.LC5
	add	x10, x10, %lo(.LC5)
	# bl	printf
	call	printf
	# mov	w0, 99
	li	x10, 99
	# str	w0, [x29, 24]
	sw	x10, 24(x8)
	# mov	w0, 10
	li	x10, 10
	# str	w0, [x29, 28]
	sw	x10, 28(x8)
	# adrp	x0, .LC6
	lui	x10, %hi(.LC6)
	# add	x0, x0, :lo12:.LC6
	add	x10, x10, %lo(.LC6)
	# bl	puts
	call	puts
	# ldr	w1, [x29, 24]
	lw	x11, 24(x8)
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# add	w1, w1, w0
	addw	x11, x11, x10
	# adrp	x0, .LC1
	lui	x10, %hi(.LC1)
	# add	x0, x0, :lo12:.LC1
	add	x10, x10, %lo(.LC1)
	# bl	printf
	call	printf
	# ldr	w1, [x29, 24]
	lw	x11, 24(x8)
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# sub	w1, w1, w0
	subw	x11, x11, x10
	# adrp	x0, .LC2
	lui	x10, %hi(.LC2)
	# add	x0, x0, :lo12:.LC2
	add	x10, x10, %lo(.LC2)
	# bl	printf
	call	printf
	# ldr	w1, [x29, 24]
	lw	x11, 24(x8)
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# mul	w1, w1, w0
	mulw	x11, x11, x10
	# adrp	x0, .LC3
	lui	x10, %hi(.LC3)
	# add	x0, x0, :lo12:.LC3
	add	x10, x10, %lo(.LC3)
	# bl	printf
	call	printf
	# ldr	w1, [x29, 24]
	lw	x11, 24(x8)
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# udiv	w1, w1, w0
	divuw	x11, x11, x10
	# adrp	x0, .LC4
	lui	x10, %hi(.LC4)
	# add	x0, x0, :lo12:.LC4
	add	x10, x10, %lo(.LC4)
	# bl	printf
	call	printf
	# ldr	w0, [x29, 24]
	lw	x10, 24(x8)
	# ldr	w1, [x29, 28]
	lw	x11, 28(x8)
	# udiv	w2, w0, w1
	divuw	x12, x10, x11
	# ldr	w1, [x29, 28]
	lw	x11, 28(x8)
	# mul	w1, w2, w1
	mulw	x11, x12, x11
	# sub	w1, w0, w1
	subw	x11, x10, x11
	# adrp	x0, .LC5
	lui	x10, %hi(.LC5)
	# add	x0, x0, :lo12:.LC5
	add	x10, x10, %lo(.LC5)
	# bl	printf
	call	printf
	# mov	w0, 0
	li	x10, 0
	# ldp	x29, x30, [sp], 32
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	addi	sp, sp, 32 # writeback
	# ret
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
