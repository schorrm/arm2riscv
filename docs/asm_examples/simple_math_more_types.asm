	.file	"simple_math_more_types.c"
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
	.string	"More checks with the sign:"
	.align	3
.LC7:
	.string	"Unsigned Ops:"
	.align	3
.LC8:
	.string	"Testing long (64 bit) signed:"
	.align	3
.LC9:
	.string	"Addition: %li\n"
	.align	3
.LC10:
	.string	"Subtraction: %li\n"
	.align	3
.LC11:
	.string	"Multiplication: %li\n"
	.align	3
.LC12:
	.string	"Division: %li\n"
	.align	3
.LC13:
	.string	"Modulus: %li\n"
	.align	3
.LC14:
	.string	"Testing long (64 bit) unsigned:"
	.align	3
.LC15:
	.string	"Addition: %lu\n"
	.align	3
.LC16:
	.string	"Subtraction: %lu\n"
	.align	3
.LC17:
	.string	"Multiplication: %lu\n"
	.align	3
.LC18:
	.string	"Division: %lu\n"
	.align	3
.LC19:
	.string	"Modulus: %lu\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	la	x21, REG_BANK
	# stp	x29, x30, [sp, -64]!
	sd	x8, -64(sp)
	sd	ra, -56(sp)
	addi	sp, sp, -64 # writeback
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
	# ldr	w0, [x29, 16]
	lw	x10, 16(x8)
	# neg	w0, w0
	sub	x10, x0, x10
	# str	w0, [x29, 16]
	sw	x10, 16(x8)
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# neg	w0, w0
	sub	x10, x0, x10
	# str	w0, [x29, 20]
	sw	x10, 20(x8)
	# adrp	x0, .LC6
	lui	x10, %hi(.LC6)
	# add	x0, x0, :lo12:.LC6
	add	x10, x10, %lo(.LC6)
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
	# adrp	x0, .LC7
	lui	x10, %hi(.LC7)
	# add	x0, x0, :lo12:.LC7
	add	x10, x10, %lo(.LC7)
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
	# mov	x0, 1
	li	x10, 1
	# str	x0, [x29, 32]
	sd	x10, 32(x8)
	# ldr	x0, [x29, 32]
	ld	x10, 32(x8)
	# lsl	x0, x0, 35
	slli	x10, x10, 35
	# str	x0, [x29, 32]
	sd	x10, 32(x8)
	# mov	x0, 1
	li	x10, 1
	# str	x0, [x29, 40]
	sd	x10, 40(x8)
	# ldr	x0, [x29, 40]
	ld	x10, 40(x8)
	# lsl	x0, x0, 34
	slli	x10, x10, 34
	# str	x0, [x29, 40]
	sd	x10, 40(x8)
	# adrp	x0, .LC8
	lui	x10, %hi(.LC8)
	# add	x0, x0, :lo12:.LC8
	add	x10, x10, %lo(.LC8)
	# bl	puts
	call	puts
	# ldr	x1, [x29, 32]
	ld	x11, 32(x8)
	# ldr	x0, [x29, 40]
	ld	x10, 40(x8)
	# add	x1, x1, x0
	add	x11, x11, x10
	# adrp	x0, .LC9
	lui	x10, %hi(.LC9)
	# add	x0, x0, :lo12:.LC9
	add	x10, x10, %lo(.LC9)
	# bl	printf
	call	printf
	# ldr	x1, [x29, 32]
	ld	x11, 32(x8)
	# ldr	x0, [x29, 40]
	ld	x10, 40(x8)
	# sub	x1, x1, x0
	sub	x11, x11, x10
	# adrp	x0, .LC10
	lui	x10, %hi(.LC10)
	# add	x0, x0, :lo12:.LC10
	add	x10, x10, %lo(.LC10)
	# bl	printf
	call	printf
	# ldr	x1, [x29, 32]
	ld	x11, 32(x8)
	# ldr	x0, [x29, 40]
	ld	x10, 40(x8)
	# mul	x1, x1, x0
	mul	x11, x11, x10
	# adrp	x0, .LC11
	lui	x10, %hi(.LC11)
	# add	x0, x0, :lo12:.LC11
	add	x10, x10, %lo(.LC11)
	# bl	printf
	call	printf
	# ldr	x1, [x29, 32]
	ld	x11, 32(x8)
	# ldr	x0, [x29, 40]
	ld	x10, 40(x8)
	# sdiv	x1, x1, x0
	div	x11, x11, x10
	# adrp	x0, .LC12
	lui	x10, %hi(.LC12)
	# add	x0, x0, :lo12:.LC12
	add	x10, x10, %lo(.LC12)
	# bl	printf
	call	printf
	# ldr	x0, [x29, 32]
	ld	x10, 32(x8)
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# sdiv	x2, x0, x1
	div	x12, x10, x11
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# mul	x1, x2, x1
	mul	x11, x12, x11
	# sub	x1, x0, x1
	sub	x11, x10, x11
	# adrp	x0, .LC13
	lui	x10, %hi(.LC13)
	# add	x0, x0, :lo12:.LC13
	add	x10, x10, %lo(.LC13)
	# bl	printf
	call	printf
	# mov	x0, 1
	li	x10, 1
	# str	x0, [x29, 48]
	sd	x10, 48(x8)
	# ldr	x0, [x29, 48]
	ld	x10, 48(x8)
	# lsl	x0, x0, 35
	slli	x10, x10, 35
	# str	x0, [x29, 48]
	sd	x10, 48(x8)
	# mov	x0, 1
	li	x10, 1
	# str	x0, [x29, 56]
	sd	x10, 56(x8)
	# ldr	x0, [x29, 56]
	ld	x10, 56(x8)
	# lsl	x0, x0, 34
	slli	x10, x10, 34
	# str	x0, [x29, 56]
	sd	x10, 56(x8)
	# adrp	x0, .LC14
	lui	x10, %hi(.LC14)
	# add	x0, x0, :lo12:.LC14
	add	x10, x10, %lo(.LC14)
	# bl	puts
	call	puts
	# ldr	x1, [x29, 32]
	ld	x11, 32(x8)
	# ldr	x0, [x29, 40]
	ld	x10, 40(x8)
	# add	x1, x1, x0
	add	x11, x11, x10
	# adrp	x0, .LC15
	lui	x10, %hi(.LC15)
	# add	x0, x0, :lo12:.LC15
	add	x10, x10, %lo(.LC15)
	# bl	printf
	call	printf
	# ldr	x1, [x29, 32]
	ld	x11, 32(x8)
	# ldr	x0, [x29, 40]
	ld	x10, 40(x8)
	# sub	x1, x1, x0
	sub	x11, x11, x10
	# adrp	x0, .LC16
	lui	x10, %hi(.LC16)
	# add	x0, x0, :lo12:.LC16
	add	x10, x10, %lo(.LC16)
	# bl	printf
	call	printf
	# ldr	x1, [x29, 32]
	ld	x11, 32(x8)
	# ldr	x0, [x29, 40]
	ld	x10, 40(x8)
	# mul	x1, x1, x0
	mul	x11, x11, x10
	# adrp	x0, .LC17
	lui	x10, %hi(.LC17)
	# add	x0, x0, :lo12:.LC17
	add	x10, x10, %lo(.LC17)
	# bl	printf
	call	printf
	# ldr	x1, [x29, 32]
	ld	x11, 32(x8)
	# ldr	x0, [x29, 40]
	ld	x10, 40(x8)
	# sdiv	x1, x1, x0
	div	x11, x11, x10
	# adrp	x0, .LC18
	lui	x10, %hi(.LC18)
	# add	x0, x0, :lo12:.LC18
	add	x10, x10, %lo(.LC18)
	# bl	printf
	call	printf
	# ldr	x0, [x29, 32]
	ld	x10, 32(x8)
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# sdiv	x2, x0, x1
	div	x12, x10, x11
	# ldr	x1, [x29, 40]
	ld	x11, 40(x8)
	# mul	x1, x2, x1
	mul	x11, x12, x11
	# sub	x1, x0, x1
	sub	x11, x10, x11
	# adrp	x0, .LC19
	lui	x10, %hi(.LC19)
	# add	x0, x0, :lo12:.LC19
	add	x10, x10, %lo(.LC19)
	# bl	printf
	call	printf
	# mov	w0, 0
	li	x10, 0
	# ldp	x29, x30, [sp], 64
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	addi	sp, sp, 64 # writeback
	# ret
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
