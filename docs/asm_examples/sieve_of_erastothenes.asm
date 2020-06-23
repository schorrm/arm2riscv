	.file	"sieve_of_erastothenes.c"
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
	.string	"prime numbers through %d are:\n"
	.align	3
.LC1:
	.string	"%d "
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	la	x21, REG_BANK
	# mov	x16, 20048
	li	x27, 20048
	# sub	sp, sp, x16
	sub	sp, sp, x27
	# stp	x29, x30, [sp]
	sd	x8, 0(sp)
	sd	ra, 8(sp)
	# add	x29, sp, 0
	addi	x8, sp, 0
	# adrp	x0, :got:__stack_chk_guard
	lui	x10, %hi(__stack_chk_guard)
	# ldr	x0, [x0, #:got_lo12:__stack_chk_guard]
	add	x10, x10, %lo(__stack_chk_guard) # load from GOT -> ADD!
	# ldr	x1, [x0]
	ld	x11, 0(x10)
	# str	x1, [x29, 20040]
	li	x26, 20040 # synthesis of oversized immediate
	add	x26, x26, x8 # converting offset register to add
	sd	x11, 0(x26)
	# mov	x1,0
	li	x11, 0
	# add	x0, x29, 32
	addi	x10, x8, 32
	# mov	x1, 20002
	li	x11, 20002
	# mov	x2, x1
	mv	x12, x11
	# mov	w1, 0
	li	x11, 0
	# bl	memset
	call	memset
	# mov	w0, 2
	li	x10, 2
	# str	w0, [x29, 20]
	sw	x10, 20(x8)
	# b	.L2
	j	.L2
.L5:
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# lsl	w0, w0, 1
	slliw	x10, x10, 1
	# str	w0, [x29, 24]
	sw	x10, 24(x8)
	# b	.L3
	j	.L3
.L4:
	# ldrsw	x0, [x29, 24]
	lw	x10, 24(x8)
	# lsl	x0, x0, 1
	slli	x10, x10, 1
	# add	x1, x29, 32
	addi	x11, x8, 32
	# mov	w2, 1
	li	x12, 1
	# strh	w2, [x1, x0]
	add	x26, x10, x11 # converting offset register to add
	sh	x12, 0(x26)
	# ldr	w1, [x29, 24]
	lw	x11, 24(x8)
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# add	w0, w1, w0
	addw	x10, x11, x10
	# str	w0, [x29, 24]
	sw	x10, 24(x8)
.L3:
	# ldr	w1, [x29, 24]
	lw	x11, 24(x8)
	# mov	w0, 10000
	li	x10, 10000
	# cmp	w1, w0
	sub	x25, x11, x10
	# ble	.L4
	ble	x25, x0, .L4
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 20]
	sw	x10, 20(x8)
.L2:
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# cmp	w0, 100
	addi	x25, x10, -100
	# ble	.L5
	ble	x25, x0, .L5
	# adrp	x0, .LC0
	lui	x10, %hi(.LC0)
	# add	x0, x0, :lo12:.LC0
	add	x10, x10, %lo(.LC0)
	# mov	w1, 10000
	li	x11, 10000
	# bl	printf
	call	printf
	# mov	w0, 2
	li	x10, 2
	# str	w0, [x29, 28]
	sw	x10, 28(x8)
	# b	.L6
	j	.L6
.L8:
	# ldrsw	x0, [x29, 28]
	lw	x10, 28(x8)
	# lsl	x0, x0, 1
	slli	x10, x10, 1
	# add	x1, x29, 32
	addi	x11, x8, 32
	# ldrsh	w0, [x1, x0]
	add	x26, x10, x11 # converting offset register to add
	lh	x10, 0(x26)
	# cmp	w0, 0
	addi	x25, x10, 0
	# bne	.L7
	bne	x25, x0, .L7
	# adrp	x0, .LC1
	lui	x10, %hi(.LC1)
	# add	x0, x0, :lo12:.LC1
	add	x10, x10, %lo(.LC1)
	# ldr	w1, [x29, 28]
	lw	x11, 28(x8)
	# bl	printf
	call	printf
.L7:
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 28]
	sw	x10, 28(x8)
.L6:
	# ldr	w1, [x29, 28]
	lw	x11, 28(x8)
	# mov	w0, 10000
	li	x10, 10000
	# cmp	w1, w0
	sub	x25, x11, x10
	# ble	.L8
	ble	x25, x0, .L8
	# mov	w0, 10
	li	x10, 10
	# bl	putchar
	call	putchar
	# mov	w0, 0
	li	x10, 0
	# adrp	x1, :got:__stack_chk_guard
	lui	x11, %hi(__stack_chk_guard)
	# ldr	x1, [x1, #:got_lo12:__stack_chk_guard]
	add	x11, x11, %lo(__stack_chk_guard) # load from GOT -> ADD!
	# ldr	x2, [x29, 20040]
	li	x26, 20040 # synthesis of oversized immediate
	add	x26, x26, x8 # converting offset register to add
	ld	x12, 0(x26)
	# ldr	x1, [x1]
	ld	x11, 0(x11)
	# eor	x1, x2, x1
	xor	x11, x12, x11
	# cmp	x1, 0
	addi	x25, x11, 0
	# beq	.L10
	beq	x25, x0, .L10
	# bl	__stack_chk_fail
	call	__stack_chk_fail
.L10:
	# ldp	x29, x30, [sp]
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	# mov	x16, 20048
	li	x27, 20048
	# add	sp, sp, x16
	add	sp, sp, x27
	# ret
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
